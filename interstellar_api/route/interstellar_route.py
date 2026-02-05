from typing import List
from fastapi import APIRouter
from model.interstellar_model import InterstellarTravelModel
from service.interstellar_service import InterstellarService


interstellar_route = APIRouter()
service = InterstellarService()


@interstellar_route.get("/info")
def get_travel_info() -> dict[str, List[str]]:
    return service.get_travel_info()


@interstellar_route.get("/type/{type}")
def get_travel_by_type(type: str) -> List[InterstellarTravelModel]:
    return service.get_travel_by_type(type)


@interstellar_route.get("/work/{work}")
def get_travel_by_work(work: str) -> List[InterstellarTravelModel]:
    return service.get_travel_by_work(work)


@interstellar_route.get("/id/{id}")
def get_travel_by_id(id: str) -> InterstellarTravelModel:
    return service.get_travel_by_id(id)
