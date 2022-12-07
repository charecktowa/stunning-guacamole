from sqlalchemy.orm import Session

from schemas.place import Place
import database.models as models


def get_places(db: Session, skip: int = 0, limit: int = 100) -> list[Place]:
    return db.query(models.Place).offset(skip).limit(limit).all()


def get_places_by_type(
    db: Session, type: str, skip: int = 0, limit: int = 3
) -> list[Place]:
    search = f"%{type}%"
    return (
        db.query(models.Place)
        .filter(models.Place.subtypes.like(search))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_place(db: Session, place_id: str) -> Place:
    return db.query(models.Place).filter(models.Place.id == place_id).first()
