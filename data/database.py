import sqlite3


class DataBase:
    def __init__(self, database_name: str):
        self.connection = sqlite3.connect(database_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute_script(self, sql_file_name: str):
        with open(sql_file_name, 'r') as f:
            return self.cursor.executescript(f.read())

    def execute(self, sql):
        return self.cursor.execute(sql)

    def commit(self):
        return self.connection.commit()

    def __del__(self):
        self.connection.close()


DATABASE = DataBase('data/cars_dealers.db')
