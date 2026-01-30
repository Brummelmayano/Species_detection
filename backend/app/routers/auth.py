from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from functools import wraps
from .. import database, models
from ..schemas import UserCreate, UserUpdate, User, Token, UserRole
from ..services.auth_service import AuthService
from ..repositories.user_repository import UserRepository
from ..utils.jwt import create_access_token, verify_token
from ..config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_role(required_role: UserRole):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="User dependency not found"
                )

            user_role = UserRole(current_user.role)
            if user_role != required_role and user_role != UserRole.ADMIN:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissions"
                )

            return await func(*args, **kwargs)
        return wrapper
    return decorator

@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: Session = Depends(database.get_db)):
    auth_service = AuthService(db)
    auth_service.create_user(user)
    # Auto-login après inscription
    from ..schemas import UserLogin
    return auth_service.login(UserLogin(username=user.username, password=user.password))

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    auth_service = AuthService(db)
    from ..schemas import UserLogin
    return auth_service.login(UserLogin(username=form_data.username, password=form_data.password))

@router.post("/logout")
async def logout():
    # JWT are stateless, logout is handled client-side
    return {"message": "Successfully logged out"}

@router.get("/me", response_model=User)
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user

@router.get("/users", response_model=List[User])
@require_role(UserRole.ADMIN)
async def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    role: UserRole = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    user_repo = UserRepository(db)
    users = user_repo.get_users(skip=skip, limit=limit)
    if role:
        users = [u for u in users if u.role == role.value]
    return users

@router.put("/users/{user_id}", response_model=User)
@require_role(UserRole.ADMIN)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    user_repo = UserRepository(db)
    user = user_repo.update_user(user_id, user_update)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
@require_role(UserRole.ADMIN)
async def delete_user(
    user_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    user_repo = UserRepository(db)
    user = user_repo.delete_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}