import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    # создание таблиц, если они не существуют
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    expense INTEGER
                )
                """
            )
            conn.commit()
    def add_name(self, name: str, expense: int):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO products (name, expense) VALUES (?, ?)
                """,
                (name, expense),
            )
            conn.commit()

    def get_products(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT name,expense FROM products 
                """
            )
            return cursor.fetchall()
    
    def total_expenses (self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute( """ 
            SELECT SUM(expense) FROM products 
            """)
            result = cursor.fetchone()
            if result [0]:
                return result[0]
            else:
                return [0]