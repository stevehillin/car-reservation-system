import mysql.connector
import os
from app import app

class DB():

    def __init__(self):
        self.db_config = {
            'host': os.environ.get('DBHOST'),
            'user': os.environ.get('DBUSER'),
            'password': os.environ.get('DBPASS'),
            'database': os.environ.get('DBNAME')
        }

    def GetConnection(self):
        return mysql.connector.connect(**self.db_config)
    
    def ExecQuery(self, query):
        try:
            conn = self.GetConnection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as err:
            app.logger.critical(str(err))
            return str(err)
        

