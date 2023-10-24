import os
import datetime
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

    # Flask Session
    # SESSION_TYPE = 'redis'
    # SESSION_PERMANENT = True
    # PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=12)
    # SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url(os.environ.get("REDIS_PATH"))

    # Others
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = "temp_data/"