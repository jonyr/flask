from flask import Flask
from src.config import BaseConfig
from src.app.routes import healthcheck_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    app.config.from_pyfile('../../instance/config.py')
    
    register_blueprints(app)
    register_extensions(app)

    return app

def register_blueprints(app: Flask):
    
    app.register_blueprint(healthcheck_bp)

def register_extensions(app):
    pass