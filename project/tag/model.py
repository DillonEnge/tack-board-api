from project import main
from project.tables import tag
from datetime import datetime
from typing import List

async def get_tag(tag_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name
        FROM
            tag
        WHERE
            id = :tag_id
            AND deleted_at IS NULL;
    """)
    values = {
        'tag_id': tag_id
    }
    return await db.fetch_one(query, values)

async def get_tags():
    db = main.get_db()
    query = ("""
        SELECT * FROM tag WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_tag(name: str):
    db = main.get_db()
    query = ("""
        INSERT INTO tag (
            id,
            name,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            clock_timestamp()
        )
        RETURNING tag.id;
    """)
    values = {
        'name': name
    }
    return await db.execute(query, values)

async def update_tag(tag_id: str, name: str):
    db = main.get_db()
    query = ("""
        UPDATE tag
            SET name = :name,
                updated_at = clock_timestamp()
        WHERE
            id = :tag_id
            AND deleted_at IS NULL
        RETURNING
            id AS tag_id,
            name AS tag_name;
    """)
    values = {
        'name': name,
        'tag_id': tag_id
    }
    return await db.execute(query, values)

async def delete_tag(tag_id: str):
    db = main.get_db()
    query = ("""
        UPDATE tag
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :tag_id
        RETURNING tag.id;
    """)
    values = {
        'tag_id': tag_id
    }
    return await db.execute(query, values)
