from sqlalchemy.orm import Session

from datetime import datetime, timezone

from . import models
from . import schemas


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).filter(models.Tag.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.dict())
    db_tag.created_at = datetime.now(timezone.utc)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


def update_tag(db: Session, tag: schemas.TagUpdate):
    db_tag = db.query(models.Tag).get(tag.id)
    db_tag.name = tag.name
    db_tag.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_tag)

    return db_tag


def delete_tag(db: Session, tag: schemas.TagDelete):
    db_tag = db.query(models.Tag).get(tag.id)
    db_tag.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_tag)

    return db_tag
