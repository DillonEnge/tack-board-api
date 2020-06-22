from project.profile.model import get_profile, get_profiles, create_profile, update_profile, delete_profile
from sanic.exceptions import ServerError
from sanic.response import json
from datetime import datetime
from typing import List
from project.email.utils import Email

#TODO Create profile_group_role schema methods to get role within group through a profile query by group_id
class Profile:
    @staticmethod
    async def get_profile(profile_id: str):
        profile = await get_profile(profile_id)

        if not profile:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'profile': {
                'id': str(profile['id']),
                'name': str(profile['name']),
                'profile_img': str(profile['profile_img']),
                'description': str(profile['description']),
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
                'profile_img': str(profile['profile_img']),
                'description': str(profile['description']),
                'phone_number': str(profile['phone_number'])
            } for profile in profiles]
        })

    @staticmethod
    async def create_profile(name: str, profile_img: str, description: str, phone_number: str, user_id: str):
        profile_id = await create_profile(name, profile_img, description, phone_number, user_id)

        if not profile_id:
            raise ServerError('u dun messd up bruther', status_code=500)
        
        return json({
            'profile_id': str(profile_id)
        })

    @staticmethod
    async def update_profile(profile_id: str, name: str, profile_img: str, description: str, phone_number: str, user_id: str):
        profile_id = await update_profile(profile_id, name, profile_img, description, phone_number, user_id)

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
