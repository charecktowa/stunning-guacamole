from sqlalchemy.orm import Session

from schemas.user import UserCreate, User, UserBase
from database.models.user import User as UserModel


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int) -> User:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_with_password(db: Session, email: str) -> UserCreate:
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
