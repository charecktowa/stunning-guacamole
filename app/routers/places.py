from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_db
from schemas.place import Place

import utils.places

router = APIRouter(prefix="/places", tags=["places"])


@router.get("/places/", response_model=list[Place])
async def read_places(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[Place]:
    if db_places := utils.places.get_places(db, skip=skip, limit=limit):
        return db_places

    raise HTTPException(404, "No se encontraron sitios")


@router.get("/places{type}/", response_model=list[Place])
async def read_places_by_type(
    type: str, skip: int = 0, limit: int = 3, db: Session = Depends(get_db)
) -> list[Place]:
    if db_place := utils.places.get_places_by_type(db, type, skip=skip, limit=limit):
        return db_place

    raise HTTPException(404, "No se encontraron sitios")


@router.get("/place{id}", response_model=Place)
async def read_place_by_id(id: str, db: Session = Depends(get_db)):
    if db_place := utils.places.get_place(db, place_id=id):
        return db_place

    raise HTTPException(404, "Sitio no encontrado")
