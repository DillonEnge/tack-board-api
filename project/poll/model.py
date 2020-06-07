from project import main
from project.tables import poll
from datetime import datetime
from typing import List

async def get_poll(poll_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            question,
            type,
            scope
        FROM
            poll
        WHERE
            id = :poll_id
            AND deleted_at IS NULL;
    """)
    values = {
        'poll_id': poll_id
    }
    return await db.fetch_one(query, values)

async def get_polls():
    db = main.get_db()
    query = ("""
        SELECT * FROM poll WHERE deleted_at IS NULL;
    """)
    return await db.fetch_all(query)

async def create_poll(question: str, poll_type: str, scope: str, event_id: str):
    db = main.get_db()
    query = ("""
        INSERT INTO poll (
            id,
            question,
            type,
            scope,
            event_id,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :question,
            :type,
            :scope,
            :event_id,
            clock_timestamp()
        )
        RETURNING poll.id;
    """)
    values = {
        'question': question,
        'type': poll_type,
        'scope': scope,
        'event_id': event_id
    }
    return await db.execute(query, values)

async def update_poll(poll_id: str, question: str, poll_type: str, scope: str, event_id: str):
    db = main.get_db()
    query = ("""
        UPDATE poll
            SET question = :question,
                type = :type,
                scope = :scope,
                event_id = :event_id,
                updated_at = clock_timestamp()
        WHERE
            id = :poll_id
            AND deleted_at IS NULL
        RETURNING
            id AS event_id,
            name AS event_name;
    """)
    values = {
        'question': question,
        'type': poll_type,
        'scope': scope,
        'event_id': event_id
    }
    return await db.execute(query, values)

async def delete_poll(poll_id: str):
    db = main.get_db()
    query = ("""
        UPDATE poll
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :poll_id
        RETURNING poll.id;
    """)
    values = {
        'poll_id': poll_id
    }
    return await db.execute(query, values)
