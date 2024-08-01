import openai
from sqlalchemy.orm import Session

from .database import get_db
from .crud import update_translation_task
from .settings import settings


def perform_translation():
    pass
