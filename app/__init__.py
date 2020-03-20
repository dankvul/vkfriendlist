from flask import Flask
from app.routes import route_gate
from config import Config


def getApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(route_gate)
    return app
