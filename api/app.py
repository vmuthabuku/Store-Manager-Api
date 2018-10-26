from flask import Flask
from .instance.config import app_config
from .v2.endpoints.user_endpoints import user_print
from .manage import create_tables

def create_app(config):
    """Receives the necessary configuration and passes to create_app"""

    app = Flask(__name__)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False
    create_tables()
    app.register_blueprint(user_print)
    return app