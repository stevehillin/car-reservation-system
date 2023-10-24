from flask import Flask, jsonify
import os
from config import Config
import logging

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY
app.session_cookie_name = Config.SECRET_KEY
session_key = os.environ.get('SECRET_KEY')


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

# Extensions
# Session(app)

# Blueprints
from modules.customers import bp as customers_bp
app.register_blueprint(customers_bp, url_prefix='/customers')

from modules.bookings import bp as bookings_bp
app.register_blueprint(bookings_bp, url_prefix='/bookings')

from modules.vehicles import bp as vehicles_bp
app.register_blueprint(vehicles_bp, url_prefix='/vehicles')

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello World'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')