from sqlalchemy.orm import Session

from schemas.user import UserCreate, User, UserBase
import database.models as models


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int) -> User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: UserCreate):