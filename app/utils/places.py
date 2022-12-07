from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from schemas.place import Place
from database.models.place import Place as PlaceModel


def get_places(db: Session, skip: int = 0, limit: int = 100) -> list[Place]:
    return db.query(PlaceModel).offset(skip).limit(limit).all()


def get_places_by_type(
    db: Session, type: str, skip: int = 0, limit: int = 3
) -> list[Place]:
    search = f"%{type}%"
    return (
        db.query(PlaceModel)
        .filter(PlaceModel.subtypes.like(search))
        .order_by(func.random())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_place(db: Session, place_id: str) -> Place:
    return db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
