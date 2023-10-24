from flask import Blueprint

bp = Blueprint('bookings', __name__)

from modules.bookings import routes