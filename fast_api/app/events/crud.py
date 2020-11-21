from sqlalchemy.orm import Session

from datetime import datetime, timezone

from typing import List

from . import models
from . import schemas
from ..tags import models as t_models


def get_events(db: Session, skip: int = 0, limit: int = 100):
    db_events = db.query(models.Event).filter(models.Event.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711

    return db_events


def create_event(db: Session, event: schemas.EventCreate):
    tag_ids = event.tags
    del event.tags
    built_tags = build_tags(db, tag_ids)
    db_event = models.Event(**event.dict())
    db_event.tags = built_tags
    db_event.created_at = datetime.now(timezone.utc)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def update_event(db: Session, event: schemas.EventOut):
    tag_ids = event.tags
    built_tags = build_tags(db, tag_ids)
    db_event = db.query(models.Event).get(event.id)
    db_event.name = event.name
    db_event.time = event.time
    db_event.location = event.location
    db_event.description = event.description
    db_event.tags = built_tags
    db_event.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_event)

    return db_event


def delete_event(db: Session, event: schemas.EventDelete):
    db_event = db.query(models.Event).get(event.id)
    db_event.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_event)

    return db_event


def build_tags(db: Session, tag_ids: List[int]):
    built_tags = []
    for tag_id in tag_ids:
        built_tags.append(db.query(t_models.Tag)
                          .filter(t_models.Tag.id == tag_id)
                          .first())

    return built_tags
