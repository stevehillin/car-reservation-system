import os
from app import app
from extensions.DB import DB

db = DB()

class Reports():

    def DailyReports():
        """Sends daily reports to employees of all bookings for today."""
        pass