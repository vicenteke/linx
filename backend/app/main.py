from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import (
    weather,
)


app = FastAPI()

# ROUTERS
app.include_router(weather.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
