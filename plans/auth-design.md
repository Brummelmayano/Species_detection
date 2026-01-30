# Conception Détaillée de l'Épic Authentification et Autorisation - Sprint 1

## Vue d'Ensemble

Cette conception détaille l'implémentation du système d'authentification et d'autorisation pour l'application de détection d'espèces. Le système doit supporter l'inscription, la connexion des utilisateurs, et la gestion des rôles avec autorisation basée sur les rôles (RBAC).

## Modèles de Base de Données

### Modèle User

```sql
-- Table des utilisateurs
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(20) NOT NULL DEFAULT 'viewer' CHECK (role IN ('viewer', 'editor', 'admin')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index pour les performances
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_role ON users(role);
```

**Champs :**
- `id` : Identifiant unique auto-incrémenté
- `email` : Adresse email unique (utilisée pour l'identification)
- `username` : Nom d'utilisateur unique
- `hashed_password` : Mot de passe hashé avec bcrypt
- `full_name` : Nom complet optionnel
- `role` : Rôle utilisateur (viewer, editor, admin)
- `is_active` : Statut d'activation du compte
- `created_at` / `updated_at` : Timestamps de création/modification

### Enumération des Rôles

```python
from enum import Enum

class UserRole(str, Enum):
    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"
```

**Permissions par rôle :**
- **Viewer** : Lecture seule (visualisation des images, résultats de détection)
- **Editor** : Upload d'images, lancement de détection, modification de ses propres données
- **Admin** : Gestion complète (utilisateurs, tous les projets, administration système)

## Schémas Pydantic

### Schémas Utilisateur

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"

class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None
    role: UserRole = UserRole.VIEWER
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8)

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[UserRole] = None
```

## Endpoints API

### Endpoints d'Authentification

#### POST /auth/register
**Description :** Inscription d'un nouvel utilisateur

**Corps de requête :**
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123",
  "full_name": "John Doe",
  "role": "viewer"
}
```

**Réponse :**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Règles métier :**
- Validation de l'unicité email/username
- Hashage du mot de passe
- Attribution automatique du rôle 'viewer' par défaut
- Connexion automatique après inscription

#### POST /auth/login
**Description :** Connexion utilisateur

**Corps de requête :**
```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Réponse :** Token JWT

**Règles métier :**
- Vérification des identifiants
- Génération du token JWT avec expiration
- Inclusion du rôle dans le payload du token

#### POST /auth/logout
**Description :** Déconnexion (invalidation du token côté client)

**Note :** Les JWT sont stateless, la déconnexion se fait côté client

#### GET /auth/me
**Description :** Récupération des informations de l'utilisateur connecté

**Headers :** `Authorization: Bearer <token>`

**Réponse :**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "role": "viewer",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Endpoints d'Administration (Admin seulement)

#### GET /auth/users
**Description :** Liste des utilisateurs (pagination)

**Query params :** `page`, `limit`, `role`

#### PUT /auth/users/{user_id}
**Description :** Modification d'un utilisateur

**Corps :** UserUpdate

#### DELETE /auth/users/{user_id}
**Description :** Désactivation d'un utilisateur

## Mécanismes de Sécurité

### JWT (JSON Web Tokens)

#### Configuration
```python
# Configuration JWT
SECRET_KEY = "your-secret-key-here"  # À définir dans les variables d'environnement
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

#### Payload du Token
```json
{
  "sub": "johndoe",
  "role": "viewer",
  "exp": 1640995200,
  "iat": 1640993400
}
```

#### Fonctions Utilitaires
```python
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None:
            raise credentials_exception
        return TokenData(username=username, role=role)
    except JWTError:
        raise credentials_exception
```

### Middleware d'Authentification

#### Dependency Injection
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    user = user_repository.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
```

### Autorisation par Rôles

#### Décorateurs de Rôles
```python
from functools import wraps
from fastapi import HTTPException, status

def require_role(required_role: UserRole):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Extraire current_user des kwargs
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="User dependency not found"
                )

            # Vérifier le rôle
            user_role = UserRole(current_user.role)
            if user_role != required_role and user_role != UserRole.ADMIN:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissions"
                )

            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Utilisation
@router.get("/admin-only")
@require_role(UserRole.ADMIN)
async def admin_endpoint(current_user: User = Depends(get_current_active_user)):
    return {"message": "Admin access granted"}
```

#### Hiérarchie des Rôles
```
Admin > Editor > Viewer

- Admin : Accès complet à toutes les fonctionnalités
- Editor : Peut créer/modifier ses propres ressources
- Viewer : Lecture seule
```

## Architecture Générale

```mermaid
graph TB
    A[Client] --> B[FastAPI]
    B --> C[Auth Router]
    B --> D[Other Routers]

    C --> E[JWT Middleware]
    E --> F[Role Authorization]

    C --> G[Auth Service]
    G --> H[User Repository]
    H --> I[PostgreSQL]

    F --> J[Role-based Access Control]
```

## Flux d'Authentification

```mermaid
sequenceDiagram
    participant Client
    participant FastAPI
    participant AuthService
    participant UserRepo
    participant Database

    Client->>FastAPI: POST /auth/register
    FastAPI->>AuthService: create_user()
    AuthService->>UserRepo: check uniqueness
    UserRepo->>Database: SELECT
    Database-->>UserRepo: result
    UserRepo-->>AuthService: ok/error
    AuthService->>AuthService: hash password
    AuthService->>UserRepo: save user
    UserRepo->>Database: INSERT
    Database-->>UserRepo: success
    UserRepo-->>AuthService: user created
    AuthService-->>FastAPI: token
    FastAPI-->>Client: JWT token

    Client->>FastAPI: POST /auth/login (with token)
    FastAPI->>AuthService: login()
    AuthService->>UserRepo: get by username
    UserRepo->>Database: SELECT
    Database-->>UserRepo: user
    UserRepo-->>AuthService: user
    AuthService->>AuthService: verify password
    AuthService-->>FastAPI: token
    FastAPI-->>Client: JWT token
```

## Dépendances et Intégrations

### Dépendances Python
```txt
fastapi==0.100.0
uvicorn==0.23.0
sqlalchemy==2.0.0
alembic==1.12.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
```

### Variables d'Environnement
```bash
DATABASE_URL=postgresql://user:password@localhost/species_db
SECRET_KEY=your-super-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Intégrations Requises
- **PostgreSQL** : Base de données principale
- **Alembic** : Migrations de base de données
- **JWT** : Gestion des tokens
- **bcrypt** : Hashage des mots de passe

## Tests et Validation

### Tests Unitaires
- Validation des schémas Pydantic
- Test des utilitaires JWT
- Test des services d'authentification

### Tests d'Intégration
- Flux complet d'inscription/connexion
- Vérification des autorisations par rôle
- Test des endpoints protégés

### Sécurité
- Audit des tokens JWT
- Validation des mots de passe
- Protection contre les attaques courantes (brute force, etc.)

## Évolution Future

### Améliorations Possibles
- Refresh tokens
- OAuth2 avec fournisseurs externes (Google, GitHub)
- Multi-factor authentication (MFA)
- Audit logging des actions administratives
- Rate limiting sur les endpoints d'authentification