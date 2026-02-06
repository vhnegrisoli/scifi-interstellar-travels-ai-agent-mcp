from fastapi import FastAPI
from route.agent_route import agent_route

app = FastAPI()

app.include_router(agent_route, prefix="/api/interstellar")
