from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Just for testing purposes
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://whattanadmin:p@ssW0rd!@172.18.0.2/whattaeat"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={},
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)

Base = declarative_base()

# DB utilities
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
