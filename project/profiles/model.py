from project import main
from project.tables import profiles
from datetime import datetime
from typing import List

async def get_profile(profile_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            icon_url,
            email,
            phone_number
        FROM
            profiles
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
        SELECT * FROM profiles WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_profile(name: str, icon_url: str, email: str, phone_number: str):
    db = main.get_db()
    query = ("""
        INSERT INTO profiles (
            id,
            name,
            icon_url,
            email,
            phone_number,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :icon_url,
            :email,
            :phone_number,
            clock_timestamp()
        )
        RETURNING profiles.id;
    """)
    values = {
        'name': name,
        'icon_url': icon_url,
        'email': email,
        'phone_number': phone_number
    }
    return await db.execute(query, values)

async def update_profile(profile_id: str, name: str, icon_url: str, email: str, phone_number: str):
    db = main.get_db()
    query = ("""
        UPDATE profiles
            SET name = :name,
                icon_url = :icon_url,
                email = :email,
                phone_number = :phone_number,
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
        'icon_url': icon_url,
        'email': email,
        'phone_number': phone_number,
        'profile_id': profile_id
    }
    return await db.execute(query, values)

async def delete_profile(profile_id: str):
    db = main.get_db()
    query = ("""
        UPDATE profiles
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :profile_id
        RETURNING id;
    """)
    values = {
        'profile_id': profile_id
    }
    return await db.execute(query, values)
