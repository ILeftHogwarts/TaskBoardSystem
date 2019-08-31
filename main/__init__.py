from flask import Flask
from main.db import init_db, close_db
from main.views import bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_mapping(test_config)
    else:
        init_db(app)
    app.register_blueprint(bp)
    app.teardown_appcontext(close_db)
    return app

