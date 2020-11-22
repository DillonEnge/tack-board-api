from sqlalchemy.orm import Session

from datetime import datetime, timezone

from . import models
from . import schemas


def get_selections(db: Session, skip: int = 0, limit: int = 100):
    db_selections = db.query(models.Selection).filter(models.Selection.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711

    return db_selections


def create_selection(db: Session, selection: schemas.SelectionCreate):
    db_selection = models.Selection(**selection.dict())
    db_selection.created_at = datetime.now(timezone.utc)
    db.add(db_selection)
    db.commit()
    db.refresh(db_selection)

    return db_selection


def update_selection(db: Session, selection: schemas.SelectionOut):
    db_selection = db.query(models.Selection).get(selection.id)
    db_selection.name = selection.name
    db_selection.poll_id = selection.poll_id
    db_selection.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_selection)

    return db_selection


def delete_selection(db: Session, selection: schemas.SelectionDelete):
    db_selection = db.query(models.Selection).get(selection.id)
    db_selection.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_selection)

    return db_selection
