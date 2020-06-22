from project.event.model import get_event, create_event, update_event, delete_event, get_event_tags, get_event_groups, add_event_tags, add_event_groups, clear_event_tags, clear_event_groups
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
        event_groups = await get_event_groups(event_id)

        if not event:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event': {
                'id': str(event['id']),
                'name': str(event['name']),
                'description': str(event['description']),
                'location': str(event['location']),
                'time': str(event['time']),
                'accessibility': str(event['accessibility']),
                'tags': [build_tag(tag) for tag in event_tags],
                'groups': [build_group(group) for group in event_groups]
            }
        })

    @staticmethod
    async def create_event(name: str, description: str, location: str, time: str, accessibility: str, tags: List[str], groups: List[str]):
        event_id = await create_event(name, description, location, time, accessibility)
        await add_event_tags(event_id, tags)
        await add_event_groups(event_id, groups)

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(event_id)
        })

    @staticmethod
    async def update_event(event_id: str, name: str, description: str, location: str, time: str, accessibility: str, tags: List[str], groups: List[str]):
        await clear_event_tags(event_id)
        await clear_event_groups(event_id)
        await add_event_tags(event_id, tags)
        await add_event_groups(event_id, groups)

        event_id = await update_event(event_id, name, description, location, time, accessibility)
        event_tags = await get_event_tags(event_id)
        event_groups = await get_event_groups(event_id)

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(event_id),
            'tags': [build_tag(tag) for tag in event_tags],
            'event_groups': [build_group(group) for group in event_groups]
        })

    @staticmethod
    async def delete_event(event_id: str):
        await clear_event_tags(event_id)
        await clear_event_groups(event_id)
        deleted_event_id = await delete_event(event_id)

        if not deleted_event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'event_id': str(deleted_event_id)
        })

def build_group(group):
    return {
        "group_id": str(group['id']),
        "group_name": str(group['name']),
        "group_description": str(group['description']),
        "group_img": str(group['group_img']),
        "group_accessibility": str(group['accessibility'])
    }

def build_tag(tag):
    return {
        "tag_id": str(tag['id']),
        "tag_name": str(tag['name'])
    }
