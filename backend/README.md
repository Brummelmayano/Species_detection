# Backend API de Détection d'Espèces

API FastAPI pour l'application de détection automatique d'espèces dans les images de pièges photographiques.

## Fonctionnalités

- **Authentification JWT** : Système de connexion sécurisé avec tokens JWT
- **Gestion des projets** : Création et gestion de projets de recherche
- **Upload d'images** : Téléchargement sécurisé d'images vers MinIO
- **Détection IA** : Intégration avec le service SpeciesNet pour la détection d'espèces
- **Base de données PostgreSQL** : Stockage persistant des métadonnées

## Architecture

L'API suit une architecture en couches :
- **Présentation** : Endpoints REST avec FastAPI
- **Métier** : Services pour la logique applicative
- **Données** : Repositories pour l'accès à la base de données

## Installation

1. **Dépendances Python** :
   ```bash
   pip install -r requirements.txt
   ```

2. **Base de données** :
   - Installer PostgreSQL
   - Créer une base de données `species_detection`
   - Configurer les variables d'environnement dans `.env`

3. **MinIO** :
   - Installer et démarrer MinIO
   - Créer un bucket `species-images`
   - Configurer les credentials dans `.env`

4. **Service SpeciesNet** :
   - Démarrer le service IA SpeciesNet sur le port 8001
   - Configurer l'URL dans `.env`

## Démarrage

```bash
python run.py
```

L'API sera disponible sur `http://localhost:8000`

## Documentation API

Une fois l'application démarrée, la documentation interactive Swagger est disponible sur :
- `http://localhost:8000/docs`

## Endpoints Principaux

### Authentification
- `POST /auth/register` : Inscription d'un nouvel utilisateur
- `POST /auth/login` : Connexion et obtention du token JWT
- `GET /auth/me` : Informations de l'utilisateur connecté

### Projets
- `GET /projects/` : Liste des projets
- `POST /projects/` : Créer un projet
- `GET /projects/{id}` : Détails d'un projet
- `PUT /projects/{id}` : Modifier un projet
- `DELETE /projects/{id}` : Supprimer un projet

### Images
- `POST /images/upload` : Uploader une image
- `GET /images/` : Liste des images
- `GET /images/{id}` : Détails d'une image
- `DELETE /images/{id}` : Supprimer une image

## Variables d'Environnement

Voir le fichier `.env` pour la configuration complète.

## Tests

```bash
pytest
```

## Développement

- Utiliser des environnements virtuels Python
- Respecter les conventions de nommage et la structure du projet
- Écrire des tests pour les nouvelles fonctionnalités
- Documenter les endpoints avec des exemples