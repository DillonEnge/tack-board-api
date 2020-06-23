from project.selection.model import get_selection, get_selections, get_selections_by_poll, create_selection, update_selection, delete_selection
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List

class Selection:
    @staticmethod
    async def get_selection(selection_id: str):
        selection = await get_selection(selection_id)

        if not selection:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'selection': {
                'id': str(selection['id']),
                'name': str(selection['name']),
                'poll_id': str(selection['poll_id'])
            }
        }

    @staticmethod
    async def get_selection_by_poll(poll_id: str):
        selections = await get_selections_by_poll(poll_id)

        return {
            'selections': [{
                'selection_id': str(selection['id']),
                'selection_name': str(selection['name'])
            } for selection in selections] 
        }

    @staticmethod
    async def get_selections():
        selections = await get_selections()

        return {
            'selections': [{
                'selection_id': str(selection['id']),
                'selection_name': str(selection['name'])
            } for selection in selections] 
        }


    @staticmethod
    async def create_selection(name: str, poll_id: str):
        selection_id = await create_selection(name, poll_id)

        if not selection_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'selection_id': str(selection_id)
        }

    @staticmethod
    async def update_selection(selection_id: str, name: str, poll_id: str):
        selection_id = await update_selection(selection_id, name, poll_id)

        if not selection_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'selection_id': str(selection_id)
        }

    @staticmethod
    async def delete_selection(selection_id: str):
        deleted_selection_id = await delete_selection(selection_id)

        if not deleted_selection_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'selection_id': str(deleted_selection_id)
        }
