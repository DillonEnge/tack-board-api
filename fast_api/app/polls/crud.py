from sqlalchemy.orm import Session

from datetime import datetime, timezone

from . import models
from . import schemas
from ..events import models as e_models


def get_polls(db: Session, skip: int = 0, limit: int = 100):
    db_polls = db.query(models.Poll).filter(models.Poll.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711

    return db_polls


def create_poll(db: Session, poll: schemas.PollCreate):
    event_id = poll.event_id
    del poll.event_id
    built_event = build_event(db, event_id)
    db_poll = models.Poll(**poll.dict())
    db_poll.event = built_event
    db_poll.created_at = datetime.now(timezone.utc)
    db.add(db_poll)
    db.commit()
    db.refresh(db_poll)

    return db_poll


def update_poll(db: Session, poll: schemas.PollOut):
    event_id = poll.event
    built_event = build_event(db, event_id)
    db_poll = db.query(models.Poll).get(poll.id)
    db_poll.question = poll.question
    db_poll.poll_type = poll.poll_type
    db_poll.poll_scope = poll.poll_scope
    db_poll.event = built_event
    db_poll.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_poll)

    return db_poll


def delete_poll(db: Session, poll: schemas.PollDelete):
    db_poll = db.query(models.Poll).get(poll.id)
    db_poll.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_poll)

    return db_poll


def build_event(db: Session, event_id: int):
    return db.query(e_models.Event).filter(e_models.Event.id == event_id).first()  # noqa: E501
