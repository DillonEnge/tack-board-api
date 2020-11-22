from sqlalchemy.orm import Session

from datetime import datetime, timezone

from . import models
from . import schemas


def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).filter(models.Group.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711


def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.dict())
    db_group.created_at = datetime.now(timezone.utc)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group


def update_group(db: Session, group: schemas.GroupUpdate):
    db_group = db.query(models.Group).get(group.id)
    db_group.name = group.name
    db_group.group_img = group.group_img
    db_group.description = group.description
    db_group.accessibility = group.accessibility
    db_group.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_group)

    return db_group


def delete_group(db: Session, group: schemas.GroupDelete):
    db_group = db.query(models.Group).get(group.id)
    db_group.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_group)

    return db_group
