import psycopg2
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        self.cursor = self.conn.cursor()

    def initialize_db(self):
        with open("init_db.sql", "r") as f:
            sql_commands = f.read().split(';')
            for command in sql_commands:
                if command.strip():
                    self.cursor.execute(command)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()