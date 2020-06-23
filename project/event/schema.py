from project.event.model import add_event_profile, clear_event_profiles, get_event, get_event_profiles, create_event, update_event, delete_event, get_event_tags, get_event_groups, add_event_tags, add_event_groups, clear_event_tags, clear_event_groups
from project.poll.schema import get_polls_by_event
from project.group.schema import Group
from project.profile.schema import Profile
from project.tag.schema import Tag
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List, Dict

class Event:
    @staticmethod
    async def get_event(event_id: str):
        event = await get_event(event_id)

        event_tags = await get_event_tags(event_id)
        event_groups = await get_event_groups(event_id)
        event_profiles = await get_event_profiles(event_id)

        if not event:
            raise ServerError('u dun messd up bruther', status_code=500)
        
        return {
            'event': {
                'id': str(event['id']),
                'name': str(event['name']),
                'description': str(event['description']),
                'location': str(event['location']),
                'time': str(event['time']),
                'accessibility': str(event['accessibility']),
                'tags': [await Tag().get_tag(tag['id']) for tag in event_tags],
                'groups': [await Group().get_group(event_group['id']) for event_group in event_groups],
                'profiles': [build_event_profile(profile) for profile in event_profiles]
            }
        }

    @staticmethod
    async def create_event(name: str, description: str, location: str, time: str, accessibility: str, tags: List[str], groups: List[str], profiles: List[Dict[str, str]]):
        event_id = await create_event(name, description, location, time, accessibility)
        await add_event_tags(event_id, tags)
        await add_event_groups(event_id, groups)

        for profile in profiles:
            await add_event_profile(event_id, profile['profile_id'], profile['role'])

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'event_id': str(event_id)
        }

    @staticmethod
    async def update_event(event_id: str, name: str, description: str, location: str, time: str, accessibility: str, tags: List[str], groups: List[str], profiles: List[Dict[str, str]]):
        await clear_event_tags(event_id)
        await clear_event_groups(event_id)
        await add_event_tags(event_id, tags)
        await add_event_groups(event_id, groups)

        await clear_event_profiles(event_id)

        for profile in profiles:
            await add_event_profile(event_id, profile['profile_id'], profile['role'])

        event_id = await update_event(event_id, name, description, location, time, accessibility)
        event_tags = await get_event_tags(event_id)
        event_groups = await get_event_groups(event_id)
        event_profiles = await get_event_profiles(event_id)

        if not event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'event_id': str(event_id),
            'tags': [await Tag().get_tag(tag['id']) for tag in event_tags],
            'groups': [await Group().get_group(event_group['id']) for event_group in event_groups],
            'profiles': [await Profile().get_profile(event_profile['id']) for event_profile in event_profiles]
        }

    @staticmethod
    async def delete_event(event_id: str):
        await clear_event_tags(event_id)
        await clear_event_groups(event_id)
        await clear_event_profiles(event_id)
        deleted_event_id = await delete_event(event_id)

        if not deleted_event_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'event_id': str(deleted_event_id)
        }

def build_event_profile(profile):
    return {
        "profile": {
            "id": str(profile['id']),
            "name": str(profile['name']),
            "profile_img": str(profile['profile_img']),
            "phone_number": str(profile['phone_number']),
            "description": str(profile['description']),
            "role": str(profile['role'])
        }
    }
