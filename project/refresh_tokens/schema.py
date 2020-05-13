from sanic.exceptions import ServerError
from project.refresh_tokens.model import get_refresh_token, create_refresh_token, update_refresh_token

class RefreshTokens:
    @staticmethod
    async def get_refresh_token(name: str):
        if not name:
            raise ServerError('u dun messd up bruther', status_code=500)

        token = await get_refresh_token(name)

        if not token:
            return None

        return {
            'token_id': str(token['id']),
            'name': str(token['name']),
            'token': str(token['token'])
        }

    @staticmethod
    async def create_refresh_token(name: str, token: str):
        if not name or not token:
            raise ServerError('u dun messd up bruther', status_code=500)

        token_id = await create_refresh_token(name, token)

        if not token_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return str(token_id)

    @staticmethod
    async def update_refresh_token(token_id: str, name: str, token: str):
        if not token_id or not name or not token:
            raise ServerError('u dun messd up bruther', status_code=500)

        token_id = await update_refresh_token(token_id, name, token)

        if not token_id:
            raise ServerError('u dun messd up bruther', status_code=500)

        return str(token_id)
