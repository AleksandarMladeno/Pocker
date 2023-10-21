import logging
import sys
import os
from logging import log
from flask import Flask
from api.poker_resource import api_poker

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api_poker, url_prefix="/api")

    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    return app


app = create_app()

if __name__ == "__main__":
    log(logging.INFO, "Starting up app_poker")
    app.run()
    log(logging.INFO, "tes")
