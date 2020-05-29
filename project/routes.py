from project import views

def setup_routes(app):

    @app.listener('before_server_start')
    def init_routes(app, loop):
        app.add_route(views.EventsView.as_view(), '/events')
        app.add_route(views.TagsView.as_view(), '/tags')
        app.add_route(views.ProfilesView.as_view(), '/profiles')
        app.add_route(views.UsersView.as_view(), '/users')
