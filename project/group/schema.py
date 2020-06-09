from project.group.model import get_group, get_groups, create_group, update_group, delete_group
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List

class Group:
    @staticmethod
    async def get_group(group_id: str):
        group = await get_group(group_id)

        if not group:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group': {
                'id': str(group['id']),
                'name': str(group['name']),
                'description': str(group['description']),
                'group_img': str(group['group_img'])
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
                'group_img': str(group['group_img'])
            } for group in groups] 
        })


    @staticmethod
    async def create_group(name: str, description: str, group_img: str):
        group_id = await create_group(name, description, group_img)

        if not group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(group_id)
        })

    @staticmethod
    async def update_group(group_id: str, name: str, description: str, group_img: str):
        group_id = await update_group(group_id, name, description, group_img)

        if not group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(group_id)
        })

    @staticmethod
    async def delete_group(group_id: str):
        deleted_group_id = await delete_group(group_id)

        if not deleted_group_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'group_id': str(deleted_group_id)
        })
