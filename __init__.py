from database.db_connector import DatabaseConnector

if __name__ == "__main__":
    db = DatabaseConnector()
    db.initialize_db()
    db.close()
    print("База данных успешно инициализирована.")