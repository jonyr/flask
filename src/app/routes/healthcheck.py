from flask import Blueprint

healthcheck_bp = Blueprint('healthchecks', __name__)

@healthcheck_bp.get('/healthcheck')
def check():
    return 'OK'