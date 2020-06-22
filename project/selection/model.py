from project import main
from project.tables import selection
from datetime import datetime
from typing import List

async def get_selection(selection_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            poll_id
        FROM
            selection
        WHERE
            id = :selection_id
            AND deleted_at IS NULL;
    """)
    values = {
        'selection_id': selection_id
    }
    return await db.fetch_one(query, values)

async def get_selections_by_poll(poll_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name
        FROM
            selection
        WHERE
            poll_id = :poll_id
            AND deleted_at IS NULL;
    """)
    values = {
        'poll_id': poll_id
    }
    return await db.fetch_all(query, values)

async def get_selections():
    db = main.get_db()
    query = ("""
        SELECT * FROM selection WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_selection(name: str, poll_id: str):
    db = main.get_db()
    query = ("""
        INSERT INTO selection (
            id,
            name,
            poll_id,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :poll_id,
            clock_timestamp()
        )
        RETURNING selection.id;
    """)
    values = {
        'name': name,
        'poll_id': poll_id
    }
    return await db.execute(query, values)

async def update_selection(selection_id: str, name: str, poll_id: str):
    db = main.get_db()
    query = ("""
        UPDATE selection
            SET name = :name,
                poll_id = :poll_id
                updated_at = clock_timestamp()
        WHERE
            id = :selection_id
            AND deleted_at IS NULL
        RETURNING
            id AS selection_id,
            name AS selection_name;
            poll_id AS poll_id
    """)
    values = {
        'name': name,
        'selection_id': selection_id,
        'poll_id': poll_id
    }
    return await db.execute(query, values)

async def delete_selection(selection_id: str):
    db = main.get_db()
    query = ("""
        UPDATE selection
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :selection_id
        RETURNING selection.id;
    """)
    values = {
        'selection_id': selection_id
    }
    return await db.execute(query, values)
