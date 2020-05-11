import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from project.settings import Settings
from environs import Env
import uuid

metadata = sqlalchemy.MetaData()
env = Env()
env.read_env()
engine = create_engine(Settings.DB_URL)
metadata.bind = engine

events = sqlalchemy.Table(
    'events',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(length=100)),
    sqlalchemy.Column('time', sqlalchemy.String(length=100)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

tags = sqlalchemy.Table(
    'tags',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

event_tags = sqlalchemy.Table(
    'event_tags',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('events.id')),
    sqlalchemy.Column('tag_id', UUID(as_uuid=True), ForeignKey('tags.id'))
)

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('icon_url', sqlalchemy.String(length=100)),
    sqlalchemy.Column('email', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('phone_number', sqlalchemy.String(length=100)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

user_tags = sqlalchemy.Table(
    'user_tags',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('user_id', UUID(as_uuid=True), ForeignKey('users.id')),
    sqlalchemy.Column('tag_id', UUID(as_uuid=True), ForeignKey('tags.id'))
)

def setup_tables():
    metadata.create_all()
