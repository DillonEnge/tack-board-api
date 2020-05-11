from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from project.events.schema import Events
from project.tags.schema import Tags
from project.users.schema import Users
from datetime import datetime


def validate_request(request: Request):
    headers = [
        'Authorization'
    ]
    print(request.headers)
    for header in headers:
        if not request.headers[header]:
            return False
    
    return True


class EventsView(HTTPMethodView):
    async def get(self, request: Request):
        event_id = request.json.get('event_id')
        event = await Events().get_event(event_id)
        return event

    async def post(self, request: Request):
        validated = validate_request(request)

        print(request.json)
        name = request.json.get('name')
        description = request.json.get('description')
        time = request.json.get('time')
        tags = request.json.get('tags')
        event_id = await Events().create_event(name, description, time, tags)
        return event_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        event_id = request.json.get('event_id')
        name = request.json.get('name')
        description = request.json.get('description')
        tags = request.json.get('tags')
        time = request.json.get('time')
        event = await Events().update_event(event_id , name, description, time, tags)
        return event

    async def delete(self, request: Request):
        validated = validate_request(request)

        event_id = request.json.get('event_id')
        deleted_event_id = await Events().delete_event(event_id)
        return deleted_event_id


class TagsView(HTTPMethodView):
    async def get(self, request: Request):
        tag_id = request.json.get('tag_id')

        if not tag_id:
            tags = await Tags().get_tags()
            return tags

        tag = await Tags().get_tag(tag_id)
        return tag

    async def post(self, request: Request):
        validated = validate_request(request)

        print(request.json)
        name = request.json.get('name')
        tag_id = await Tags().create_tag(name)
        return tag_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        tag_id = request.json.get('tag_id')
        name = request.json.get('name')
        tag = await Tags().update_tag(tag_id , name)
        return tag

    async def delete(self, request: Request):
        validated = validate_request(request)

        tag_id = request.json.get('tag_id')
        deleted_tag_id = await Tags().delete_tag(tag_id)
        return deleted_tag_id


class UsersView(HTTPMethodView):
    async def get(self, request: Request):
        user_id = request.json.get('user_id')

        if not user_id:
            users = await Users().get_users()
            return users

        user = await Users().get_user(user_id)
        return user

    async def post(self, request: Request):
        validated = validate_request(request)

        print(request.json)
        name = request.json.get('name')
        icon_url = request.json.get('icon_url')
        email = request.json.get('email')
        phone_number = request.json.get('phone_number')
        user_id = await Users().create_user(name, icon_url, email, phone_number)
        return user_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        user_id = request.json.get('user_id')
        name = request.json.get('name')
        icon_url = request.json.get('icon_url')
        email = request.json.get('email')
        phone_number = request.json.get('phone_number')

        user = await Users().update_user(user_id , name, icon_url, email, phone_number)
        return user

    async def delete(self, request: Request):
        validated = validate_request(request)

        user_id = request.json.get('user_id')
        deleted_user_id = await Users().delete_user(user_id)
        return deleted_user_id
