from project import main
from project.tables import users
from datetime import datetime
from typing import List

async def get_user(user_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            users.id AS id,
            users.name AS name,
            users.icon_url AS icon_url,
            users.email AS email,
            users.phone_number AS phone_number
        FROM
            users
        WHERE
            users.id = :user_id
            AND users.deleted_at IS NULL;
    """)
    values = {
        'user_id': user_id
    }
    return await db.fetch_one(query, values)

async def get_users():
    db = main.get_db()
    query = ("""
        SELECT * FROM users WHERE users.deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_user(name: str, icon_url: str, email: str, phone_number: str):
    db = main.get_db()
    query = ("""
        INSERT INTO users (
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
        RETURNING users.id;
    """)
    values = {
        'name': name,
        'icon_url': icon_url,
        'email': email,
        'phone_number': phone_number
    }
    return await db.execute(query, values)

async def update_user(user_id: str, name: str, icon_url: str, email: str, phone_number: str):
    db = main.get_db()
    query = ("""
        UPDATE users
            SET name = :name,
                icon_url = :icon_url,
                email = :email,
                phone_number = :phone_number,
                updated_at = clock_timestamp()
        WHERE
            users.id = :user_id
            AND users.deleted_at IS NULL
        RETURNING
            users.id AS event_id,
            users.name AS event_name;
    """)
    values = {
        'name': name,
        'icon_url': icon_url,
        'email': email,
        'phone_number': phone_number,
        'user_id': user_id
    }
    return await db.execute(query, values)

async def delete_user(user_id: str):
    db = main.get_db()
    query = ("""
        UPDATE users
            SET deleted_at = clock_timestamp()
        WHERE 
            users.id = :user_id
        RETURNING users.id;
    """)
    values = {
        'user_id': user_id
    }
    return await db.execute(query, values)
