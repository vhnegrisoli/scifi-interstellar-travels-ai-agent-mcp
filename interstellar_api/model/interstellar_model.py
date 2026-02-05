from pydantic import BaseModel


class InterstellarTravelModel(BaseModel):
    id: str
    type: str
    work: str
    description: str
