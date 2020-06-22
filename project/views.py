from sanic.exceptions import ServerError
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from project.event.schema import Event
from project.tag.schema import Tag
from project.group.schema import Group
from project.selection.schema import Selection
from project.profile.schema import Profile
from project.user.schema import User
from project.poll.schema import Poll
from datetime import datetime


def validate_request(request: Request):
    headers = [
        'Authorization'
    ]

    for header in headers:
        if not request.headers[header]:
            return False
    
    return True


class EventsView(HTTPMethodView):
    async def get(self, request: Request):
        event_id = request.json.get('event_id')
        event = await Event().get_event(event_id)
        return event

    async def post(self, request: Request):
        validated = validate_request(request)

        name = request.json.get('name')
        description = request.json.get('description')
        location = request.json.get('location')
        time = request.json.get('time')
        accessibility = request.json.get('accessibility')
        tags = request.json.get('tags')
        groups = request.json.get('groups')
        event_id = await Event().create_event(name, description, location, time, accessibility, tags, groups)
        return event_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        event_id = request.json.get('event_id')
        name = request.json.get('name')
        description = request.json.get('description')
        location = request.json.get('location')
        time = request.json.get('time')
        accessibility = request.json.get('accessibility')
        tags = request.json.get('tags')
        groups = request.json.get('groups')
        event = await Event().update_event(event_id , name, description, time, accessibility, tags, groups)
        return event

    async def delete(self, request: Request):
        validated = validate_request(request)

        event_id = request.json.get('event_id')
        deleted_event_id = await Event().delete_event(event_id)
        return deleted_event_id


class TagsView(HTTPMethodView):
    async def get(self, request: Request):
        tag_id = request.json.get('tag_id')

        if not tag_id:
            tags = await Tag().get_tags()
            return tags

        tag = await Tag().get_tag(tag_id)
        return tag

    async def post(self, request: Request):
        validated = validate_request(request)

        name = request.json.get('name')
        tag_id = await Tag().create_tag(name)
        return tag_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        tag_id = request.json.get('tag_id')
        name = request.json.get('name')
        tag = await Tag().update_tag(tag_id , name)
        return tag

    async def delete(self, request: Request):
        validated = validate_request(request)

        tag_id = request.json.get('tag_id')
        deleted_tag_id = await Tag().delete_tag(tag_id)
        return deleted_tag_id

class GroupsView(HTTPMethodView):
    async def get(self, request: Request):
        group_id = request.json.get('group_id')

        if not group_id:
            groups = await Group().get_groups()
            return groups

        group = await Group().get_group(group_id)
        return group

    async def post(self, request: Request):
        validated = validate_request(request)

        name = request.json.get('name')
        description = request.json.get('description')
        group_img = request.json.get('group_img')
        accessibility = request.json.get('accessibility')
        if 'profiles' not in request.json:
            raise ServerError('u furgot the profiles', status_code=500)
        profiles = request.json.get('profiles')
        group_id = await Group().create_group(name, description, group_img, accessibility, profiles)
        return group_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        group_id = request.json.get('group_id')
        name = request.json.get('name')
        description = request.json.get('description')
        group_img = request.json.get('group_img')
        accessibility = request.json.get('accessibility')
        if 'profiles' not in request.json:
            raise ServerError('u furgot the profiles', status_code=500)
        profiles = request.json.get('profiles')
        group = await Group().update_group(group_id, name, description, group_img, accessibility, profiles)
        return group

    async def delete(self, request: Request):
        validated = validate_request(request)

        group_id = request.json.get('group_id')
        deleted_group_id = await Group().delete_group(group_id)
        return deleted_group_id

class SelectionsView(HTTPMethodView):
    async def get(self, request: Request):
        selection_id = request.json.get('selection_id')

        poll_id = request.json.get('poll_id')
        if poll_id:
            selections = await Selection().get_selection_by_poll(poll_id)
            return selections

        if not selection_id:
            selections = await Selection().get_selections()
            return selections

        selection = await Selection().get_selection(selection_id)
        return selection

    async def post(self, request: Request):
        validated = validate_request(request)

        name = request.json.get('name')
        poll_id = request.json.get('poll_id')
        selection_id = await Selection().create_selection(name, poll_id)
        return selection_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        selection_id = request.json.get('selection_id')
        name = request.json.get('name')
        poll_id = request.json.get('poll_id')
        selection = await Selection().update_selection(selection_id, name, poll_id)
        return selection

    async def delete(self, request: Request):
        validated = validate_request(request)

        selection_id = request.json.get('selection_id')
        deleted_selection_id = await Group().delete_selection(selection_id)
        return deleted_selection_id


class ProfilesView(HTTPMethodView):
    async def get(self, request: Request):
        profile_id = request.json.get('profile_id')

        if not profile_id:
            profiles = await Profile().get_profiles()
            return profiles

        profile = await Profile().get_profile(profile_id)
        return profile

    async def post(self, request: Request):
        validated = validate_request(request)

        name = request.json.get('name')
        profile_img = request.json.get('profile_img')
        description = request.json.get('description')
        phone_number = request.json.get('phone_number')
        user_id = request.json.get('user_id')
        profile_id = await Profile().create_profile(name, profile_img, description, phone_number, user_id)
        return profile_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        profile_id = request.json.get('profile_id')
        name = request.json.get('name')
        profile_img = request.json.get('profile_img')
        description = request.json.get('description')
        phone_number = request.json.get('phone_number')
        user_id = request.json.get('user_id')
        profile = await Profile().update_profile(profile_id , name, profile_img, description, phone_number, user_id)
        return profile

    async def delete(self, request: Request):
        validated = validate_request(request)

        profile_id = request.json.get('profile_id')
        deleted_profile_id = await Profile().delete_profile(profile_id)
        return deleted_profile_id

class UsersView(HTTPMethodView):
    async def get(self, request: Request):
        user_id = request.json.get('user_id')

        if not user_id:
            user = await User().get_users()
            return user

        user = await User().get_user(user_id)
        return user

    async def post(self, request: Request):
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user_id = await User().create_user(username, password, email)
        return user_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        user_id = request.json.get('user_id')
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user = await User().update_user(user_id , username, password, email)
        return user

    async def delete(self, request: Request):
        validated = validate_request(request)

        user_id = request.json.get('user_id')
        deleted_user_id = await User().delete_user(user_id)
        return deleted_user_id

class PollsView(HTTPMethodView):
    async def get(self, request: Request):
        poll_id = request.json.get('poll_id')
        event_id = request.json.get('event_id')
        if event_id:
            polls = await Poll().get_polls_by_event(event_id)
            return polls

        if not poll_id:
            polls = await Poll().get_polls()
            return polls

        poll = await Poll().get_poll(poll_id)
        return poll

    async def post(self, request: Request):
        validated = validate_request(request)

        question = request.json.get('question')
        poll_type = request.json.get('type')
        scope = request.json.get('scope')
        event_id = request.json.get('event_id')
        poll_id = await Poll().create_poll(question, poll_type, scope, event_id)
        return poll_id

    async def patch(self, request: Request):
        validated = validate_request(request)

        poll_id = request.json.get('poll_id')
        question = request.json.get('question')
        poll_type = request.json.get('type')
        scope = request.json.get('scope')
        event_id = request.json.get('event_id')
        poll = await Poll().update_poll(poll_id, question, poll_type, scope, event_id)
        return poll

    async def delete(self, request: Request):
        validated = validate_request(request)

        poll_id = request.json.get('poll_id')
        deleted_poll_id = await Poll().delete_poll(poll_id)
        return deleted_poll_id
