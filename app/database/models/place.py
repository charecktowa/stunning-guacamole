from ..db_setup import Base

from sqlalchemy import Column, Text

# TODO: Change this to Mongo maybe, don't know
class Place(Base):
    __tablename__ = "place"

    id = Column(Text, primary_key=True)
    name = Column(Text)
    site = Column(Text)
    type = Column(Text)
    subtypes = Column(Text)
    phone = Column(Text)
    full_address = Column(Text)
    country = Column(Text)
    latitude = Column(Text)
    longitude = Column(Text)
    rating = Column(Text)
    reviews = Column(Text)
    reviews_link = Column(Text)
    photo = Column(Text)
    working_hours = Column(Text)
    range = Column(Text)
    description = Column(Text)
    location_link = Column(Text)
