import psycopg2 as db
from typing import Tuple

class Connection:
    def __init__(self, db_password):
        self.postgres = {
            "host": "172.17.0.2",
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
            input(f"\n{sql}")
            self.execute(sql)
            self.commit()

        except Exception as error:
            input(f"\n{error}")

    # READ
    def read(self, table: str, filter: str, columns_to_search: str = '*'):
        try:
            sql = f"SELECT {columns_to_search} FROM {table} WHERE {filter}"
            input(f"\n{sql}")
            return self.query(sql)

        except Exception as error:
            input(f"\n{error}")

    def read_all(self, table: str, columns: str = '*'):
        try:
            sql = f"SELECT {columns} FROM {table}"
            input(f"\n{sql}")
            return self.query(sql)

        except Exception as error:
            input(f"\n{error}")

    # UPDATE
    def update(self, table: str, filter: str, column_to_set: str, value_to_set: str):
        try:
            sql = f"UPDATE {table} SET {column_to_set} = {value_to_set} WHERE {filter}"
            input(f"\n{sql}")
            self.execute(sql)
            self.commit()

        except Exception as error:
            input(f"\n{error}")

    # DELETE
    def delete(self, table: str, filter: str):
        try:
            sql = f"DELETE FROM {table} WHERE {filter}"
            input(f"\n{sql}")
            self.execute(sql)
            self.commit()

        except Exception as error:
            input(f"\n{error}")


    def obter_relatorio_produtos(self):
        try:
            # Crie um cursor para executar as consultas

            # Consulta para obter o relatório de produtos
            consulta = """
                SELECT NomeProduto, Descricao, Preco, EstoqueDisponivel, Preco * EstoqueDisponivel AS ValorTotalEstoque
                FROM public.Produtos;
            """
            self.execute(consulta)

            # Recupere os resultados da consulta
            relatorio = self.fetchall()

            # Exiba o relatório
            for produto in relatorio:
                print("Nome do Produto:", produto[0])
                print("Descrição:", produto[1])
                print("Preço:", produto[2])
                print("Estoque Disponível:", produto[3])
                print("Valor Total do Estoque:", produto[4])
                print("-" * 30)

        except Exception as e:
            print("Erro ao executar a consulta:", e)
