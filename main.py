import os
from database.db_connector import DatabaseConnector
#from gui.main_window import MainWindow
#from logic.auth import Auth
#from logic.time_tracker import TimeTracker

def initialize_application():
    """
    Инициализация приложения:
    - Подключение к базе данных.
    - Инициализация базы данных (создание таблиц, если их нет).
    - Запуск графического интерфейса.
    """
    # Инициализация базы данных
    db = DatabaseConnector()
    db.initialize_db()


if __name__ == "__main__":
    # Запуск приложения
    initialize_application()