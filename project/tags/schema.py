from project.tags.model import get_tag, get_tags, create_tag, update_tag, delete_tag
from sanic.response import json
from datetime import datetime
from typing import List

class Tags:
    @staticmethod
    async def get_tag(tag_id: str):
        tag = await get_tag(tag_id)

        if not tag:
            raise Exception('u dun messd up bruther')

        return json({
            'tag': {
                'id': str(tag['id']),
                'name': str(tag['name'])
            }
        })
    
    @staticmethod
    async def get_tags():
        tags = await get_tags()

        return json({
            'tags': [{
                'tag_id': str(tag['id']),
                'tag_name': str(tag['name'])
            } for tag in tags] 
        })


    @staticmethod
    async def create_tag(name: str):
        tag_id = await create_tag(name)

        if not tag_id:
            raise Exception('u dun messd up bruther')

        return json({
            'tag_id': str(tag_id)
        })

    @staticmethod
    async def update_tag(tag_id: str, name: str):
        tag_id = await update_tag(tag_id, name)

        if not tag_id:
            raise Exception('u dun messd up bruther')

        return json({
            'tag_id': str(tag_id)
        })

    @staticmethod
    async def delete_tag(tag_id: str):
        deleted_tag_id = await delete_tag(tag_id)

        if not deleted_tag_id:
            raise Exception('u dun messd up bruther')

        return json({
            'tag_id': str(deleted_tag_id)
        })
