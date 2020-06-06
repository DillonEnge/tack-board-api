from project import main
from project.tables import user
from datetime import datetime
from typing import List

async def get_user(user_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            username,
            password,
            email
        FROM
            "user"
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
            password,
            email
        FROM
            "user"
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
        SELECT * FROM "user" WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_user(username: str, password: str, email: str):
    db = main.get_db()
    query = ("""
        INSERT INTO "user" (
            id,
            username,
            password,
            email,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :username,
            :password,
            :email,
            clock_timestamp()
        )
        RETURNING id;
    """)
    values = {
        'username': username,
        'password': password,
        'email': email
    }
    return await db.execute(query, values)

async def update_user(user_id: str, username: str, password: str, email: str):
    db = main.get_db()
    query = ("""
        UPDATE "user"
            SET username = :username,
                password = :password,
                email = :email,
                updated_at = clock_timestamp()
        WHERE
            id = :user_id
            AND deleted_at IS NULL
        RETURNING
            id AS user_id,
            username AS user_name;
    """)
    values = {
        'username': name,
        'password': password,
        'email': email,
        'user_id': user_id
    }
    return await db.execute(query, values)

async def delete_user(user_id: str):
    db = main.get_db()
    query = ("""
        UPDATE "user"
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :user_id
        RETURNING id;
    """)
    values = {
        'user_id': user_id
    }
    return await db.execute(query, values)
