from connection import Connection
from utils import *

class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = get_db_password()
        self.connect = Connection(db_password)

        while True:
            display_menu()
            choice = input("Digite sua escolha: ").upper()

            if choice == 'C':
                sys_clear()
                display_header(header="C")
                # Get table name from the user
                table_name = input("Digite o nome da tabela: ").upper()
                # Get column name from the user
                table_cols = get_table_columns(table_name)
                print(f"Colunas: {table_cols}\n")
                # Get values from the user as a comma-separated
                values = tuple(v.strip() for v in input("Digite os valores das colunas no formato acima (value1, value2):\n").split(','))
                self.connect.create(
                    table_name,
                    table_cols,
                    values
                )

            elif choice == 'R':
                while True:
                    display_header(header="R")
                    display_read_options()
                    choice = input("Digite sua escolha: ")

                    if choice == '1':
                        sys_clear()
                        display_header('R-A')
                        # Get table name from the user
                        table_name = input("Digite o nome da tabela: ").upper()
                        table_cols = get_table_columns(table_name)
                        print(f"Colunas: {table_cols}\n")
                        columns_to_search = input("Digite os nomes das colunas que deseja exibir: ")
                        data = self.connect.read_all(table_name, columns_to_search)
                        if data is not None:
                            print(f"\n{table_cols}\n")
                            for row in data:
                                print(row)
                            input()

                    elif choice == '2':
                        sys_clear()
                        display_header('R-F')
                        # Get table name from the user
                        table_name = input("Digite o nome da tabela: ").upper()
                        table_cols = get_table_columns(table_name)
                        print(f"Colunas: {table_cols}\n")
                        columns_to_search = input("Digite os nomes das colunas que deseja exibir: ")
                        filter = input("Digite o argumento de filtragem (Coluna :op Valor): ")
                        data = self.connect.read(
                            table_name,
                            filter,
                            columns_to_search
                        )
                        if data is not None:
                            print(f"\n{table_cols}\n")
                            for row in data:
                                print(row)
                            input()

                    elif choice == 'S':
                        break

            elif choice == 'U':
                sys_clear()
                display_header(header="U")
                # Get table name from the user
                table_name = input("Digite o nome da tabela: ").upper()
                columns = get_table_columns(table_name)
                print(f"Colunas: {columns}\n")
                # Get value from the user
                filter = input("Digite o argumento de filtragem (Coluna :op Valor): ")
                column_to_set = input("Digite o nome da coluna a ser modificada: ")
                value_to_set = input("Digite o novo valor para a coluna: ")
                self.connect.update(
                    table_name,
                    filter,
                    column_to_set,
                    value_to_set
                )

            elif choice == 'D':
                sys_clear()
                display_header(header='D')
                # Get table name from the user
                table_name = input("Digite o nome da tabela: ").upper()
                columns = get_table_columns(table_name)
                print(f"Colunas: {columns}\n")
                # Get value from the user
                filter = input("Digite o argumento de filtragem (Coluna :op Valor): ")
                self.connect.delete(
                    table_name,
                    filter
                )

            elif choice == 'S':
                input("\nSaindo da área restrita...")
                input("Saindo da área restrita...")
                break
            
            elif choice == 'RLP':
                self.connect.obter_relatorio_produtos()
                input()

    def read_options(self):
        while True:
            display_read_options()
            choice = input("Digite sua escolha: ")

            if choice == '1':
                sys_clear()
                display_header('R-A')
                # Get table name from the user
                table_name = input("Digite o nome da tabela: ").upper()
                table_cols = get_table_columns(table_name)
                print(f"Colunas: {table_cols}\n")
                columns_to_search = input("Digite os nomes das colunas que deseja exibir: ")
                data = self.connect.read_all(table_name, columns_to_search)
                print(f"\n{table_cols}\n")
                for row in data:
                    print(row)
                input()

            elif choice == '2':
                sys_clear()
                display_header('R-F')
                # Get table name from the user
                table_name = input("Digite o nome da tabela: ").upper()
                table_cols = get_table_columns(table_name)
                print(f"Colunas: {table_cols}\n")
                columns_to_search = input("Digite os nomes das colunas que deseja exibir: ")
                filter = input("Digite o argumento de filtragem (Coluna :op Valor): ")
                data = self.connect.read(
                    table_name,
                    filter,
                    columns_to_search
                )
                print(f"\n{table_cols}\n")
                for row in data:
                    print(row)
                input()

            elif choice == 'S':
                break
