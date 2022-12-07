import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db_setup import engine
from database.models import user, place

from routers import places

user.Base.metadata.create_all(bind=engine)
place.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stunning Guacamole - Whattaeat API",
    description="API para autenticar y obtener distintos lugares para comer",
    version="0.1.0",
    contact={
        "name": "Alfredo",
        "email": "charecktowa@protonmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(places.router)


@app.get("/")
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
