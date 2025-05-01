import sqlite3

class Database:
    def __init__(self, path: str ):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXIST films(
                id INTEGER PRIMARY KEY AUTOINCERMENT,
                name TEXT,
                style TEXT
                year TEXT
                )
                """
            )
            conn.commit

    def add_films(self, name: str, style:str , year:str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO films (name,style,year) VALUES (?,?)
                """,
                (name,style,year),
            )
            conn.commit()
    def all_films(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM films")
            return cursor.fetchall()
        
    def get_one_film(self, id : str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM films WHERE id = ?",id)

    def delete_films(self, id : int):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FEOM films WHERE id = ?", (id))
            conn.commit()

    def update_film(self, id:int,name:str,style:str,year:str):
        with sqlite3.connect(self.path) as conn:
            conn.execute("UPDATE films SET name=?,style=?,year=? WHERE id=?",
                         (id, name , style ,year))
            conn.commit()
                   