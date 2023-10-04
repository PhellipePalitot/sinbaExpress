import psycopg2 as db
from typing import Tuple

class Connection:
    def __init__(self, db_password):
        self.postgres = {
            "host": "localhost",
            "port": "5432",
            "user": "postgres",
            "password": db_password,
            "database": "postgres"
        }

        try:
            self.conn = db.connect(**self.postgres)
            self.cur = self.conn.cursor()
        except Exception as error:
            print("Error connecting to postgres database", error)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def commit(self):
        return self.conn.commit()

    def fetchall(self):
        return self.cur.fetchall()

    # executa o comando SQL
    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())

    # executa o comando SQL e dá o fetchall pra pegar os resultados desse comando
    def query(self, sql, params=None):
        self.cur.execute(str(sql), params or ())
        return self.fetchall()

    # CREATE
    def create(self, table: str, columns: str, values: Tuple):
        try:
            sql = f"INSERT INTO {table} ({columns}) VALUES {values}"
            input(sql)
            self.execute(sql)
            self.commit()

        except Exception as error:
            input("Error inserting record in {table}", error)

    # READ
    def read(self, table: str, filter: str, columns_to_search: str = '*'):
        try:
            sql = f"SELECT {columns_to_search} FROM {table} WHERE {filter}"
            input(sql)
            return self.query(sql)

        except Exception as error:
            input(f"Record not found in {table}", error)

    def read_all(self, table: str, columns: str = '*'):
        try:
            sql = f"SELECT {columns} FROM {table}"
            input(sql)
            return self.query(sql)

        except Exception as error:
            input(f"Record not found in {table}", error)

    # UPDATE
    def update(self, table: str, filter: str, column_to_set: str, value_to_set: str):
        try:
            sql = f"UPDATE {table} SET {column_to_set} = {value_to_set} WHERE {filter}"
            input(sql)
            self.execute(sql)
            self.commit()

        except Exception as error:
            input("Error updating {table}", error)

    # DELETE
    def delete(self, table: str, filter: str):
        try:
            sql = f"DELETE FROM {table} WHERE {filter}"
            input(sql)
            self.execute(sql)
            self.commit()

        except Exception as error:
            input(f"Error deleting record(s) from {table}: {error}")
