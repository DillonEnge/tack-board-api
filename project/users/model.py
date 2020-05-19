from project import main
from project.tables import users
from datetime import datetime
from typing import List

async def get_user(user_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            username,
            password
        FROM
            users
        WHERE
            id = :user_id
            AND deleted_at IS NULL;
    """)
    values = {
        'user_id': user_id
    }
    return await db.fetch_one(query, values)

async def get_user_by_name(username: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            username,
            password
        FROM
            users
        WHERE
            username = :username
            AND deleted_at IS NULL;
    """)
    values = {
        'username': username
    }
    return await db.fetch_one(query, values)

async def get_users():
    db = main.get_db()
    query = ("""
        SELECT * FROM users WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_user(username: str, password: str):
    db = main.get_db()
    query = ("""
        INSERT INTO users (
            id,
            username,
            password,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :username,
            :password,
            clock_timestamp()
        )
        RETURNING users.id;
    """)
    values = {
        'username': username,
        'password': password
    }
    return await db.execute(query, values)

async def update_user(user_id: str, name: str, icon_url: str, email: str, phone_number: str):
    db = main.get_db()
    query = ("""
        UPDATE users
            SET username = :username,
                password = :password,
                updated_at = clock_timestamp()
        WHERE
            id = :user_id
            AND deleted_at IS NULL
        RETURNING
            users.id AS user_id,
            users.name AS user_name;
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
            id = :user_id
        RETURNING users.id;
    """)
    values = {
        'user_id': user_id
    }
    return await db.execute(query, values)
