from typing import Optional
from pydantic import BaseModel


class Place(BaseModel):
    id: Optional[str] = None
    site: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    subtypes: Optional[str] = None
    phone: Optional[str] = None
    full_address: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    rating: Optional[str] = None
    reviews: Optional[str] = None
    reviews_link: Optional[str] = None
    photo: Optional[str] = None
    working_hours: Optional[str] = None
    range: Optional[str] = None
    description: Optional[str] = None
    location_link: Optional[str] = None

    class Config:
        orm_mode = True
