from sqlalchemy.orm import Session
from . import models


def create_translation_task(db: Session, text: str, languages: list):
    task = models.TranslationTask(text=text, languages=languages)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_translation_task(db: Session, task_id: int):
    task = (
        db.query(models.TranslationTask)
        .filter(models.TranslationTask.task_id == task_id)
        .first()
    )

    return task


def update_translation_task(db: Session, task_id: int, translations: dict):
    task = get_translation_task(db, task_id)

    task.translations = translations
    task.status = "completed"

    db.commit()
    db.refresh(task)

    return task
