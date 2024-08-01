from sqlalchemy import Integer, String, Column, JSON, DateTime
from .database import Base
from datetime import datetime


class TranslationTask(Base):
    __tablename__ = "translation_task"

    task_id = Column(Integer, primary_key=True)

    text = Column(String, nullable=False)
    languages = Column(JSON, nullable=False)

    translations = Column(JSON, default={})

    status = Column(String, nullable=False, default="in progress")

    # created_at = Column(DateTime, default=datetime.utcnow())
    # updated_at = Column(DateTime, onupdate=datetime.utcnow())
