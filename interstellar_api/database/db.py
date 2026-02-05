import json
from typing import List
from model.interstellar_model import InterstellarTravelModel
from pathlib import Path


_LOADED_DB: List[InterstellarTravelModel] | None = None
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "interstellar_db.json"


def init_db():
    global _LOADED_DB
    if _LOADED_DB is None:
        _LOADED_DB = _load_data()


def get_db() -> List[InterstellarTravelModel]:
    if _LOADED_DB is None:
        print("Database not initialized. Initializing...")
        init_db()
    else:
        print("Database loaded with", len(_LOADED_DB), "records.")
    return _LOADED_DB


def _load_data() -> List[InterstellarTravelModel]:
    with open(DB_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    db_data = data.get("interstellar_travel_db", [])
    return [_to_model(item) for item in db_data]


def _to_model(item: dict) -> InterstellarTravelModel:
    return InterstellarTravelModel(
        id=item["id"],
        type=item["type"],
        work=item["work"],
        description=item["description"]
    )
