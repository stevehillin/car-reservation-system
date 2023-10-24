import os
from app import app
from extensions.DB import DB

db = DB()

class Documents():

    def GenerateInvoice(booking_id: str):
        """Generates and invoice to later send to customer."""
        pass

    def GenerateConfirmationLetter(booking_id: str):
        """Generates confirmation letter to send to customer."""
        pass