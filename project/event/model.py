from project import main
from project.tables import event
from datetime import datetime
from typing import List

async def get_event(event_id: str):
    db = main.get_db()
    query = ("""
        SELECT
            id,
            name,
            description,
            location,
            time
        FROM
            event
        WHERE
            id = :event_id
            AND deleted_at IS NULL;
    """)
    values = {
        'event_id': event_id
    }
    return await db.fetch_one(query, values)

async def create_event(name: str, description: str, location: str, time: str):
    db = main.get_db()
    query = ("""
        INSERT INTO event (
            id,
            name,
            description,
            location,
            time,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :description,
            :location,
            :time,
            clock_timestamp()
        )
        RETURNING event.id;
    """)
    values = {
        'name': name,
        'description': description,
        'location': location,
        'time': time
    }
    return await db.execute(query, values)

async def update_event(event_id: str, name: str, description: str, location: str, time: str):
    db = main.get_db()
    query = ("""
        UPDATE event
            SET name = :name,
                description = :description,
                location = :location
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
        'location': location,
        'time': time,
        'event_id': event_id,
    }
    return await db.execute(query, values)

async def delete_event(event_id: str):
    db = main.get_db()
    query = ("""
        UPDATE event
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
            tag.id,
            tag.name
        FROM
            event_tag,
            tag
        WHERE
            event_tag.event_id = :event_id
            AND event_tag.tag_id = tag.id;
    """)
    values = {
        'event_id': event_id
    }
    return await db.fetch_all(query, values)

async def add_event_tags(event_id: str, tags: List[str]):
    db = main.get_db()
    if len(tags) > 0:
        query = ("""
            INSERT INTO event_tag (id, event_id, tag_id)
            SELECT
                uuid_generate_v4(),
                (SELECT id from event
                    WHERE id = :event_id AND deleted_at IS NULL),
                id
            FROM
                tag
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
            event_tag
        WHERE
            event_id = :event_id;
    """)
    values = {
        "event_id": event_id
    }
    return await db.execute(query, values)
