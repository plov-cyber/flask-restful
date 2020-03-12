from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from data import db_session
from data.users_resource import UsersResource, UsersListResource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init('db/blogs.sqlite')
    api = Api(app)
    api.add_resource(UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(UsersListResource, '/api/v2/users/')
    app.run()


if __name__ == '__main__':
    main()
