from flask import Flask
from main.db import init_db
from main.views import bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    init_db(app)
    app.register_blueprint(bp)
    return app
