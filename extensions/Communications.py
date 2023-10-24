import os
from app import app
from extensions.DB import DB

db = DB()

class Communications():

    def __init__(self):
        self.config = {
            'mailhost': os.environ.get('MAILHOST'),
            'user': os.environ.get('MAILUSER'),
            'password': os.environ.get('DBPASS'),
        }

    def SendEmail(self, destination: str, document_id: str):
        """Used to send various emails and documents to customers and employees as needed."""
        pass