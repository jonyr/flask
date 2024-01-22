from flask import Flask
from src.app.routes import healthcheck_bp

def create_app():
    app = Flask(__name__)
    
    register_blueprint(healthcheck_bp)
    register_extensions(app)

    return app

def register_blueprints(app):
    app.register_blueprint(healthcheck_bp)

def register_extensions(app):
    pass