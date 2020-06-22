from project import main
from project.tables import profile
from datetime import datetime
from typing import List

async def get_profile(profile_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            profile_img,
            description,
            phone_number
        FROM
            profile
        WHERE
            id = :profile_id
            AND deleted_at IS NULL;
    """)
    values = {
        'profile_id': profile_id
    }
    return await db.fetch_one(query, values)

async def get_profiles():
    db = main.get_db()
    query = ("""
        SELECT * FROM profile WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_profile(name: str, profile_img: str, description: str, phone_number: str, user_id: str):
    db = main.get_db()
    query = ("""
        INSERT INTO profile (
            id,
            name,
            profile_img,
            description,
            phone_number,
            user_id,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :profile_img,
            :description,
            :phone_number,
            :user_id,
            clock_timestamp()
        )
        RETURNING profile.id;
    """)
    values = {
        'name': name,
        'profile_img': profile_img,
        'description': description,
        'phone_number': phone_number,
        'user_id': user_id
    }
    return await db.execute(query, values)

async def update_profile(profile_id: str, name: str, profile_img: str, description: str, phone_number: str, user_id: str):
    db = main.get_db()
    query = ("""
        UPDATE profile
            SET name = :name,
                profile_img = :profile_img,
                description = :description,
                phone_number = :phone_number,
                user_id = :user_id
                updated_at = clock_timestamp()
        WHERE
            id = :profile_id
            AND deleted_at IS NULL
        RETURNING
            id AS profile_id,
            name AS profile_name;
    """)
    values = {
        'name': name,
        'profile_img': profile_img,
        'description': description,
        'phone_number': phone_number,
        'profile_id': profile_id,
        'user_id': user_id
    }
    return await db.execute(query, values)

async def delete_profile(profile_id: str):
    db = main.get_db()
    query = ("""
        UPDATE profile
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :profile_id
        RETURNING id;
    """)
    values = {
        'profile_id': profile_id
    }
    return await db.execute(query, values)
