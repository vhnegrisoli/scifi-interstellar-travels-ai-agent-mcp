from typing import List
from database.db import get_db
from model.interstellar_model import InterstellarTravelModel


class InterstellarRepository:

    def __init__(self):
        self._db = get_db()

    def get_ids(self) -> List[str]:
        return set([item.id for item in self._db])

    def get_types(self) -> List[str]:
        return set([item.type for item in self._db])

    def get_works(self) -> List[str]:
        return set([item.work for item in self._db])

    def get_by_type(self, type: str) -> List[InterstellarTravelModel]:
        return [item for item in self._db if item.type == type]

    def get_by_work(self, work: str) -> List[InterstellarTravelModel]:
        return [item for item in self._db if item.work == work]

    def get_by_id(self, id: str) -> InterstellarTravelModel | None:
        for item in self._db:
            if item.id == id:
                return item
        return None
