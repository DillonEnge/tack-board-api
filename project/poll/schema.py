from project.poll.model import get_poll, get_polls, get_polls_by_event, create_poll, update_poll, delete_poll
from project.selection.model import get_selections_by_poll
from sanic.response import json
from sanic.exceptions import ServerError
from datetime import datetime
from typing import List

class Poll:
    @staticmethod
    async def get_poll(poll_id: str):
        poll = await get_poll(poll_id)

        if not poll:
            raise ServerError('u dun messd up bruther', status_code=500)
        
        selections = await get_selections_by_poll(poll_id)

        return {
            'poll': {
                'id': str(poll['id']),
                'question': str(poll['question']),
                'type': str(poll['type']),
                'scope': str(poll['scope']),
                'selections': [{
                    'name': str(selection['name'])
                } for selection in selections]
            }
        }
    
    @staticmethod
    async def get_polls():
        polls = await get_polls()

        return {
            'polls': [{
                'poll_id': str(poll['id']),
                'poll_question': str(poll['question']),
                'poll_type': str(poll['type']),
                'poll_scope': str(poll['scope'])
            } for poll in polls] 
        }

    @staticmethod
    async def get_polls_by_event(event_id: str):
        polls = await get_polls_by_event(event_id)

        built_polls_arr = []
        for poll in polls:
            selections = await get_selections_by_poll(poll['id'])
            built_polls_arr.append({
                'id': str(poll['id']),
                'question': str(poll['question']),
                'type': str(poll['type']),
                'scope': str(poll['scope']),
                'selections': [{
                    'name': str(selection['name'])
                } for selection in selections]
            })

        return {
            'polls': built_polls_arr
        }

    @staticmethod
    async def create_poll(question: str, poll_type: str, scope: str, event_id: str):
        poll_id = await create_poll(question, poll_type, scope, event_id)

        if not poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'poll_id': str(poll_id)
        }

    @staticmethod
    async def update_poll(poll_id: str, question: str, poll_type: str, scope: str, event_id: str):
        poll_id = await update_poll(poll_id, question, poll_type, scope, event_id)

        if not poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'poll_id': str(poll_id)
        }

    @staticmethod
    async def delete_poll(poll_id: str):
        deleted_poll_id = await delete_poll(poll_id)

        if not deleted_poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return {
            'poll_id': str(deleted_poll_id)
        }
