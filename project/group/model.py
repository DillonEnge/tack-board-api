from project import main
from project.tables import group
from datetime import datetime
from typing import List

async def get_group(group_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            description,
            group_img
        FROM
            "group"
        WHERE
            id = :group_id
            AND deleted_at IS NULL;
    """)
    values = {
        'group_id': group_id
    }
    return await db.fetch_one(query, values)

async def get_groups():
    db = main.get_db()
    query = ("""
        SELECT * FROM "group" WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_group(name: str, description: str, group_img: str):
    db = main.get_db()
    query = ("""
        INSERT INTO "group" (
            id,
            name,
            description,
            group_img,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :description,
            :group_img,
            clock_timestamp()
        )
        RETURNING id;
    """)
    values = {
        'name': name,
        'description': description,
        'group_img': group_img
    }
    return await db.execute(query, values)

async def update_group(group_id: str, name: str, description: str, group_img: str):
    db = main.get_db()
    query = ("""
        UPDATE "group"
            SET name = :name,
                description = :description,
                group_img = :group_img,
                updated_at = clock_timestamp()
        WHERE
            id = :group_id
            AND deleted_at IS NULL
        RETURNING
            id AS group_id,
            name AS group_name;
    """)
    values = {
        'name': name,
        'group_id': group_id
    }
    return await db.execute(query, values)

async def delete_group(group_id: str):
    db = main.get_db()
    query = ("""
        UPDATE "group"
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :group_id
        RETURNING id;
    """)
    values = {
        'group_id': group_id
    }
    return await db.execute(query, values)
