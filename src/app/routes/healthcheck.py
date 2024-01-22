from flask import Blueprint

healthcheck_bp = Blueprint('healthcheck', __name__)

healthcheck_bp.get('/healthcheck')
def check():
    return 'OK'