from project.users.model import get_user, get_user_by_name, get_users, create_user, update_user, delete_user
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List

class Users:
    @staticmethod
    async def get_user(user_id: str, retrieving_user=False):
        user = await get_user(user_id)

        if not user:
            raise ServerError('u dun messd up bruther', status_code=500)
        
        if retrieving_user:
            return {
                'user_id': str(user['id']),
                'username': str(user['username']),
                'password': str(user['password'])
            }

        return json({
            'user': {
                'id': str(user['id']),
                'username': str(user['username']),
                'password': str(user['password'])
            }
        })

    @staticmethod
    async def get_user_by_name(username: str):
        user = await get_user_by_name(username)

        if not user:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'user_id': str(user['id']), # Important key for use with sanic_jwt
            'username': str(user['username']),
            'password': str(user['password'])
        }

    @staticmethod
    async def get_users():
        users = await get_users()

        return json({
            'users': [{
                'id': str(user['id']),
                'username': str(user['username']),
                'password': str(user['password'])
            } for user in users]
        })

    @staticmethod
    async def create_user(username: str, password: str):
        user_id = await create_user(username, password)

        if not user_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'user_id': str(user_id)
        })

    @staticmethod
    async def update_user(user_id: str, username: str, password: str):
        user_id = await update_user(user_id, username, password)

        if not user_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'user_id': str(user_id)
        })

    @staticmethod
    async def delete_user(user_id: str):
        deleted_user_id = await delete_user(user_id)

        if not deleted_user_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'user_id': str(deleted_user_id)
        })
