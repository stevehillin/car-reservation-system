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
        retval = {'status': 'error', 'data': ''}
        try:
            conn = self.GetConnection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                retval['status'] = 'ok'
                retval['data'] = result
            cursor.close()
            conn.close()
            
        except mysql.connector.Error as err:
            app.logger.critical(f"Mysql Error: {str(err)}")
            retval['data'] = str(err)
        return retval

    def ExecUpdate(self, query, data=False):
        retval = {'status': 'error', 'data': ''}
        try:
            conn = self.GetConnection()
            cursor = conn.cursor(prepared=True)
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            conn.commit()
            rowcount = cursor.rowcount
            retval['status'] = 'ok'
            retval['data'] = f'{rowcount} record(s) affected.'
            cursor.close()
            conn.close()
            
        except mysql.connector.Error as err:
            app.logger.critical(f"Mysql Error: {str(err)}")
            retval['data'] = str(err)
        return retval