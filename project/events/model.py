from project import main
from project.tables import events
from datetime import datetime
from typing import List

async def get_event(event_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            description,
            time
        FROM
            events
        WHERE
            id = :event_id
            AND deleted_at IS NULL;
    """)
    values = {
        'event_id': event_id
    }
    return await db.fetch_one(query, values)

async def create_event(name: str, description: str, time: str):
    db = main.get_db()
    query = ("""
        INSERT INTO events (
            id,
            name,
            description,
            time,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :description,
            :time,
            clock_timestamp()
        )
        RETURNING events.id;
    """)
    values = {
        'name': name,
        'description': description,
        'time': time
    }
    return await db.execute(query, values)

async def update_event(event_id: str, name: str, description: str, time: str):
    db = main.get_db()
    query = ("""
        UPDATE events
            SET name = :name,
                description = :description,
                time = :time,
                updated_at = clock_timestamp()
        WHERE
            id = :event_id
            AND deleted_at IS NULL
        RETURNING
            id AS event_id,
            name AS event_name,
            description AS event_description,
            time AS event_time;
    """)
    values = {
        'name': name,
        'description': description,
        'time': time,
        'event_id': event_id,
    }
    return await db.execute(query, values)

async def delete_event(event_id: str):
    db = main.get_db()
    query = ("""
        UPDATE events
            SET deleted_at = clock_timestamp()
        WHERE 
            id = :event_id
        RETURNING id;
    """)
    values = {
        'event_id': event_id
    }
    return await db.execute(query, values)

async def get_event_tags(event_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            tags.id,
            tags.name
        FROM
            event_tags,
            tags
        WHERE
            event_tags.event_id = :event_id
            AND event_tags.tag_id = tags.id;
    """)
    values = {
        'event_id': event_id
    }
    return await db.fetch_all(query, values)

async def add_event_tags(event_id: str, tags: List[str]):
    db = main.get_db()
    if len(tags) > 0:
        query = ("""
            INSERT INTO event_tags (id, event_id, tag_id)
            SELECT
                uuid_generate_v4(),
                (SELECT id from events
                    WHERE id = :event_id AND deleted_at IS NULL),
                id
            FROM
                tags
            WHERE
                id = ANY(:tags);
        """)
        values = {
            "event_id": event_id,
            "tags": tags
        }
        return await db.execute(query, values)

async def clear_event_tags(event_id: str):
    db = main.get_db()
    query = ("""
        DELETE FROM
            event_tags
        WHERE
            event_id = :event_id;
    """)
    values = {
        "event_id": event_id
    }
    return await db.execute(query, values)
