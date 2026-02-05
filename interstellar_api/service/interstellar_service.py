from typing import List
from model.interstellar_model import InterstellarTravelModel
from repository.interstellar_repository import InterstellarRepository


class InterstellarService:

    def __init__(self):
        self._repository = InterstellarRepository()

    def get_travel_info(self) -> dict[str, List[str]]:
        ids = self._repository.get_ids()
        types = self._repository.get_types()
        works = self._repository.get_works()
        return {
            "ids": ids,
            "types": types,
            "works": works
        }

    def get_travel_by_type(self, type: str) -> List[InterstellarTravelModel]:
        return self._repository.get_by_type(type)

    def get_travel_by_work(self, work: str) -> List[InterstellarTravelModel]:
        return self._repository.get_by_work(work)

    def get_travel_by_id(self, id: str) -> InterstellarTravelModel:
        return self._repository.get_by_id(id)
