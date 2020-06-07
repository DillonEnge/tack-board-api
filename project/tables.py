import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from project.settings import Settings
from environs import Env
import uuid

metadata = sqlalchemy.MetaData()
env = Env()
env.read_env()
engine = create_engine(Settings.DB_URL)
metadata.bind = engine

type_enum = ("checklist", "description")
scope_enum = ("moderator_only", "all_members")

event = sqlalchemy.Table(
    'event',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(length=100)),
    sqlalchemy.Column('time', sqlalchemy.String(length=100)),
    sqlalchemy.Column('location', sqlalchemy.String(length=100)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

tag = sqlalchemy.Table(
    'tag',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

event_tag = sqlalchemy.Table(
    'event_tag',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('tag_id', UUID(as_uuid=True), ForeignKey('tag.id'))
)

group = sqlalchemy.Table(
    'group',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('description', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('group_img', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

poll = sqlalchemy.Table(
    'poll',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('question', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('type', Enum("checklist", "description", name="poll_type")),
    sqlalchemy.Column('scope', Enum("moderator_only", "all_members", name="poll_scope")),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

profile = sqlalchemy.Table(
    'profile',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('profile_img', sqlalchemy.String(length=100)),
    sqlalchemy.Column('phone_number', sqlalchemy.String(length=100)),
    sqlalchemy.Column('description', sqlalchemy.String(length=100)),
    sqlalchemy.Column('user_id', UUID(as_uuid=True), ForeignKey('user.id')),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

user = sqlalchemy.Table(
    'user',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

refresh_token = sqlalchemy.Table(
    'refresh_token',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('token', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

def setup_tables():
    metadata.create_all()

def get_metadata():
    return metadata

def get_type_enum():
    return type_enum

def get_scope_enum():
    return scope_enum