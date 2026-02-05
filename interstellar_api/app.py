from fastapi import FastAPI
from database.db import init_db
from route.interstellar_route import interstellar_route

app = FastAPI()

init_db()

app.include_router(interstellar_route, prefix="/api/interstellar")