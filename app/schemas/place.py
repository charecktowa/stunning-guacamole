from pydantic import BaseModel


class Place(BaseModel):
    id: str
    site: str
    name: str
    type: str
    subtypes: str
    phone: str
    full_address: str
    country: str
    latitude: str
    longitude: str
    rating: str
    reviews: str
    reviews_link: str
    photo: str
    working_hours: str
    range: str
    description: str
    location_link: str

    class Config:
        orm_mode = True
