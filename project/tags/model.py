from project import main
from project.tables import tags
from datetime import datetime
from typing import List

async def get_tag(tag_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            tags.id AS id,
            tags.name AS name
        FROM
            tags
        WHERE
            tags.id = :tag_id
            AND tags.deleted_at IS NULL;
    """)
    values = {
        'tag_id': tag_id
    }
    return await db.fetch_one(query, values)

async def get_tags():
    db = main.get_db()
    query = ("""
        SELECT * FROM tags WHERE tags.deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_tag(name: str):
    db = main.get_db()
    query = ("""
        INSERT INTO tags (
            id,
            name,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            clock_timestamp()
        )
        RETURNING tags.id;
    """)
    values = {
        'name': name
    }
    return await db.execute(query, values)

async def update_tag(tag_id: str, name: str):
    db = main.get_db()
    query = ("""
        UPDATE tags
            SET name = :name,
                updated_at = clock_timestamp()
        WHERE
            tags.id = :tag_id
            AND tags.deleted_at IS NULL
        RETURNING
            tags.id AS event_id,
            tags.name AS event_name;
    """)
    values = {
        'name': name,
        'tag_id': tag_id
    }
    return await db.execute(query, values)

async def delete_tag(tag_id: str):
    db = main.get_db()
    query = ("""
        UPDATE tags
            SET deleted_at = clock_timestamp()
        WHERE 
            tags.id = :tag_id
        RETURNING tags.id;
    """)
    values = {
        'tag_id': tag_id
    }
    return await db.execute(query, values)
