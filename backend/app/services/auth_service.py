from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models
from ..schemas import UserCreate, UserLogin
from ..utils.jwt import verify_password, get_password_hash, create_access_token
from ..repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def authenticate_user(self, username: str, password: str):
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    def create_user(self, user: UserCreate):
        # Vérifier si l'utilisateur existe déjà
        db_user = self.user_repo.get_user_by_email(user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email déjà enregistré")
        db_user = self.user_repo.get_user_by_username(user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Nom d'utilisateur déjà pris")

        # Créer l'utilisateur
        hashed_password = get_password_hash(user.password)
        user_data = user.dict()
        user_data["hashed_password"] = hashed_password
        del user_data["password"]

        return self.user_repo.create_user(user_data)

    def login(self, user_credentials: UserLogin):
        user = self.authenticate_user(user_credentials.username, user_credentials.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Nom d'utilisateur ou mot de passe incorrect",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_access_token(data={"sub": user.username, "role": user.role})
        return {"access_token": access_token, "token_type": "bearer"}