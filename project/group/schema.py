from project.group.model import add_group_profile, get_group, get_group_profiles, get_groups, create_group, clear_group_profiles, update_group, delete_group
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List, Dict

class Group:
    @staticmethod
    async def get_group(group_id: str):
        group = await get_group(group_id)

        group_profiles = await get_group_profiles(group_id)

        if not group:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group': {
                'id': str(group['id']),
                'name': str(group['name']),
                'description': str(group['description']),
                'group_img': str(group['group_img']),
                'accessibility': str(group['accessibility']),
                'profiles': [build_group_profile(profile) for profile in group_profiles]
            }
        })
    
    @staticmethod
    async def get_groups():
        groups = await get_groups()

        return json({
            'groups': [{
                'group_id': str(group['id']),
                'group_name': str(group['name']),
                'group_description': str(group['description']),
                'group_img': str(group['group_img']),
                'group_accessibility': str(group['accessibility'])
            } for group in groups] 
        })


    @staticmethod
    async def create_group(name: str, description: str, group_img: str, accessibility: str, profiles: List[Dict[str, str]]):
        group_id = await create_group(name, description, group_img, accessibility)
        for profile in profiles:
            await add_group_profile(group_id, profile['profile_id'], profile['role'])

        if not group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(group_id)
        })

    @staticmethod
    async def update_group(group_id: str, name: str, description: str, group_img: str, accessibility: str, profiles: List[Dict[str, str]]):
        group_id = await update_group(group_id, name, description, group_img, accessibility)
        await clear_group_profiles(group_id)
        for profile in profiles:
            await add_group_profile(group_id, profile['profile_id'], profile['role'])

        group_profiles = await get_group_profiles(group_id)

        if not group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(group_id),
            'profiles': [build_group_profile(profile) for profile in group_profiles]
        })

    @staticmethod
    async def delete_group(group_id: str):
        deleted_group_id = await delete_group(group_id)

        if not deleted_group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(deleted_group_id)
        })

def build_group_profile(profile):
    return {
        "profile_id": str(profile['id']),
        "profile_name": str(profile['name']),
        "profile_img": str(profile['profile_img']),
        "profile_phone_number": str(profile['phone_number']),
        "profile_description": str(profile['description']),
        "profile_role": str(profile['role'])
    }
