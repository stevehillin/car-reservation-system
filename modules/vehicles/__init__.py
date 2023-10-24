from flask import Blueprint

bp = Blueprint('vehicles', __name__)

from modules.vehicles import routes