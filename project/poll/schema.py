from project.poll.model import get_poll, get_polls, create_poll, update_poll, delete_poll
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

        return json({
            'poll': {
                'id': str(poll['id']),
                'question': str(poll['question']),
                'type': str(poll['type']),
                'scope': str(poll['scope'])
            }
        })
    
    @staticmethod
    async def get_polls():
        polls = await get_polls()

        return json({
            'polls': [{
                'poll_id': str(poll['id']),
                'poll_question': str(poll['question']),
                'poll_type': str(poll['type']),
                'poll_scope': str(poll['scope'])
            } for poll in polls] 
        })


    @staticmethod
    async def create_poll(question: str, poll_type: str, scope: str, event_id: str):
        poll_id = await create_poll(question, poll_type, scope, event_id)

        if not poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'poll_id': str(poll_id)
        })

    @staticmethod
    async def update_poll(poll_id: str, question: str, poll_type: str, scope: str, event_id: str):
        poll_id = await update_poll(poll_id, question, poll_type, scope, event_id)

        if not poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'poll_id': str(poll_id)
        })

    @staticmethod
    async def delete_poll(poll_id: str):
        deleted_poll_id = await delete_poll(poll_id)

        if not deleted_poll_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return json({
            'poll_id': str(deleted_poll_id)
        })
