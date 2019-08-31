from flask import Blueprint
from flask.views import MethodView

# Init blueprint
main = Blueprint('main', __name__, url_prefix='/api')


class MainView(MethodView):
    def get(self, user_name):
        return {
            'msg': 'Hello from main page updated'
            if user_name is None else
            f'Hello mr {user_name}'
        }


main_view = MainView.as_view('main')

# Register method view
main.add_url_rule(
    '/',
    view_func=main_view,
    methods=['GET'],
    endpoint='main',
    defaults={'user_name': None}
)

main.add_url_rule(
    '/<string:user_name>',
    view_func=main_view,
    endpoint='main',
    methods=['GET']
)
