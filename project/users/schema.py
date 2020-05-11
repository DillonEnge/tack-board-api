from project.users.model import get_user, get_users, create_user, update_user, delete_user
from sanic.response import json
from datetime import datetime
from typing import List

class Users:
    @staticmethod
    async def get_user(user_id: str):
        user = await get_user(user_id)

        if not user:
            raise Exception('u dun messd up bruther')

        return json({
            'user': {
                'id': str(user['id']),
                'name': str(user['name']),
                'icon_url': str(user['icon_url']),
                'email': str(user['email']),
                'phone_number': str(user['phone_number'])
            }
        })

    @staticmethod
    async def get_users():
        users = await get_users()

        return json({
            'users': [{
                'id': str(user['id']),
                'name': str(user['name']),
                'icon_url': str(user['icon_url']),
                'email': str(user['email']),
                'phone_number': str(user['phone_number'])
            } for user in users]
        })

    @staticmethod
    async def create_user(name: str, icon_url: str, email: str, phone_number: str):
        user_id = await create_user(name, icon_url, email, phone_number)

        if not user_id:
            raise Exception('u dun messd up bruther')

        return json({
            'user_id': str(user_id)
        })

    @staticmethod
    async def update_user(user_id: str, name: str, icon_url: str, email: str, phone_number: str):
        user_id = await update_user(user_id, name, icon_url, email, phone_number)

        if not user_id:
            raise Exception('u dun messd up bruther')

        return json({
            'user_id': str(user_id)
        })

    @staticmethod
    async def delete_user(user_id: str):
        deleted_user_id = await delete_user(user_id)

        if not deleted_user_id:
            raise Exception('u dun messd up bruther')

        return json({
            'user_id': str(deleted_user_id)
        })
