from flask import Flask, request
from flask_smorest import Api
from resources.roam import blp as orderDataBlueprint


def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "ROAM-API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    api = Api(app)
    api.register_blueprint(orderDataBlueprint)
    return app


