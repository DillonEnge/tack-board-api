from project.profiles.model import get_profile, get_profiles, create_profile, update_profile, delete_profile
from sanic.exceptions import ServerError
from sanic.response import json
from datetime import datetime
from typing import List
from project.email.utils import Email

class Profiles:
    @staticmethod
    async def get_profile(profile_id: str):
        profile = await get_profile(profile_id)

        if not profile:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'profile': {
                'id': str(profile['id']),
                'name': str(profile['name']),
                'icon_url': str(profile['icon_url']),
                'email': str(profile['email']),
                'phone_number': str(profile['phone_number'])
            }
        })

    @staticmethod
    async def get_profiles():
        profiles = await get_profiles()

        return json({
            'profiles': [{
                'id': str(profile['id']),
                'name': str(profile['name']),
                'icon_url': str(profile['icon_url']),
                'email': str(profile['email']),
                'phone_number': str(profile['phone_number'])
            } for profile in profiles]
        })

    @staticmethod
    async def create_profile(name: str, icon_url: str, email: str, phone_number: str):
        profile_id = await create_profile(name, icon_url, email, phone_number)

        if not profile_id:
            raise ServerError('u dun messd up bruther', status_code=500)
        
        return json({
            'profile_id': str(profile_id)
        })

    @staticmethod
    async def update_profile(profile_id: str, name: str, icon_url: str, email: str, phone_number: str):
        profile_id = await update_profile(profile_id, name, icon_url, email, phone_number)

        if not profile_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'profile_id': str(profile_id)
        })

    @staticmethod
    async def delete_profile(profile_id: str):
        deleted_profile_id = await delete_profile(profile_id)

        if not deleted_profile_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'profile_id': str(deleted_profile_id)
        })
