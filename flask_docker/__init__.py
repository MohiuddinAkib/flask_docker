from flask import Flask
from flask_docker.routes.main import main


def create_app(config_file='settings.py'):
    # Init app
    app = Flask(__name__)
    # Set app config
    app.config.from_pyfile(config_file)
    # Register blueprint
    app.register_blueprint(main)
    return app


if __name__ == '__main__':
    create_app()
