from sanic_jwt import exceptions
from project.user.schema import User
from project.refresh_token.schema import RefreshToken

async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = await User().get_user_by_name(username)

    if password != user.get('password'):
        raise exceptions.AuthenticationFailed()

    return user

async def store_refresh_token(user_id, refresh_token, *args, **kwargs):
    name = f'refresh_token_{user_id}'
    token = await RefreshToken().get_refresh_token(name)
    if token:
        await RefreshToken().update_refresh_token(token['token_id'], name, refresh_token)
    else:
        await RefreshToken().create_refresh_token(name, refresh_token)

async def retrieve_refresh_token(request, user_id, *args, **kwargs):
    name = f'refresh_token_{user_id}'
    token = await RefreshToken().get_refresh_token(name)
    return token['token']

async def retrieve_user(request, payload, *args, **kwargs):
    if payload:
        user_id = payload.get('user_id', None)
        user = await User().get_user(user_id, retrieving_user=True)
        print(f'user:{user}')
        return user
    else:
        return None