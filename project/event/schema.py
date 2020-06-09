from project.event.model import get_event, create_event, update_event, delete_event, get_event_tags, add_event_tags, clear_event_tags
from project.poll.schema import get_polls_by_event
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List

class Event:
    @staticmethod
    async def get_event(event_id: str):
        event = await get_event(event_id)

        event_tags = await get_event_tags(event_id)

        if not event:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event': {
                'id': str(event['id']),
                'name': str(event['name']),
                'description': str(event['description']),
                'location': str(event['location']),
                'time': str(event['time']),
                'tags': [build_tag(tag) for tag in event_tags]
            }
        })

    @staticmethod
    async def create_event(name: str, description: str, location: str, time: str, tags: List[str]):
        event_id = await create_event(name, description, location, time)
        await add_event_tags(event_id, tags)

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(event_id)
        })

    @staticmethod
    async def update_event(event_id: str, name: str, description: str, location: str, time: str, tags: List[str]):
        await clear_event_tags(event_id)
        await add_event_tags(event_id, tags)

        event_id = await update_event(event_id, name, description, location, time)
        event_tags = await get_event_tags(event_id)

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(event_id),
            'tags': [build_tag(tag) for tag in event_tags]
        })

    @staticmethod
    async def delete_event(event_id: str):
        await clear_event_tags(event_id)
        deleted_event_id = await delete_event(event_id)

        if not deleted_event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(deleted_event_id)
        })

def build_tag(tag):
    return {
        "tag_id": str(tag['id']),
        "tag_name": str(tag['name'])
    }
