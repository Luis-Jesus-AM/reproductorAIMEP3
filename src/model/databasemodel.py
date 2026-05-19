import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.config = {
            "host": "127.0.0.1",
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "port": 3306
        }

    def get_connection(self):
        return mysql.connector.connect(**self.config)

    def execute_query(self, sql, params=None, fetchone=False, fetchall=False):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        
        result = None
        if fetchone:
            result = cursor.fetchone()
        elif fetchall:
            result = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()
        return result
