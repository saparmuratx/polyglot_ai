from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime


class TranslationRequest(BaseModel):
    text: str
    languages: List[str]


class TaskResponse(BaseModel):
    task_id: int

    created_at: datetime


class TranslationStatus(BaseModel):
    task_id: int
    text: str
    languages: List
    status: str
    translations: Dict[str, str]
