from sanic import Sanic
from sanic_jwt import Initialize

from databases import Database

from environs import Env
from project.routes import setup_routes
from project.settings import Settings
from project.middlewares import setup_middlewares
from project.tables import setup_tables
from project.authentication import (authenticate,
                                    store_refresh_token,
                                    retrieve_refresh_token,
                                    retrieve_user)

app = Sanic(__name__)
Initialize(
    app,
    authenticate=authenticate,
    refresh_token_enabled=True,
    store_refresh_token=store_refresh_token,
    retrieve_refresh_token=retrieve_refresh_token,
    retrieve_user=retrieve_user
)

def setup_database():
    app.db = Database(app.config.DB_URL)

    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()

def get_db() -> Database:
    return app.db

def init():
    env = Env()
    env.read_env()

    app.config.from_object(Settings)

    setup_database()
    setup_tables()
    setup_routes(app)
    setup_middlewares(app)

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
