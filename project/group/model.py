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
            group_img,
            accessibility
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

async def create_group(name: str, description: str, group_img: str, accessibility: str):
    db = main.get_db()
    query = ("""
        INSERT INTO "group" (
            id,
            name,
            description,
            group_img,
            accessibility,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :description,
            :group_img,
            :accessibility,
            clock_timestamp()
        )
        RETURNING id;
    """)
    values = {
        'name': name,
        'description': description,
        'group_img': group_img,
        'accessibility': accessibility
    }
    return await db.execute(query, values)

async def update_group(group_id: str, name: str, description: str, group_img: str, accessibility: str):
    db = main.get_db()
    query = ("""
        UPDATE "group"
            SET name = :name,
                description = :description,
                group_img = :group_img,
                accessibility = :accessibility
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

async def get_group_profiles(group_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            profile.id,
            profile.name,
            profile.profile_img,
            profile.phone_number,
            profile.description,
            profile_group_role.role
        FROM
            profile_group_role,
            profile
        WHERE
            profile_group_role.group_id = :group_id
            AND profile_group_role.profile_id = profile.id;
    """)
    values = {
        'group_id': group_id
    }
    return await db.fetch_all(query, values)

async def add_group_profile(group_id: str, profile_id: str, role: str):
    db = main.get_db()
    query = ("""
        INSERT INTO profile_group_role (id, profile_id, group_id, role)
        SELECT
            uuid_generate_v4(),
            profile.id,
            :group_id,
            :role
        FROM
            profile
        WHERE
            id = :profile_id
    """)
    values = {
        "group_id": group_id,
        "profile_id": profile_id,
        "role": role
    }
    return await db.execute(query, values)
 
async def clear_group_profiles(group_id: str):
    db = main.get_db()
    query = ("""
        DELETE FROM
            profile_group_role
        WHERE
            group_id = :group_id;
    """)
    values = {
        "group_id": group_id
    }
    return await db.execute(query, values)
