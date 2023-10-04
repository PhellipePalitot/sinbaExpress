import getpass
import os
from connection import Connection

table_columns = {
    "CLIENTES": "Nome, CPF, Endereco, Email, Telefone, Usuario",
    "PRODUTOS": "NomeProduto, Descricao, Preco, EstoqueDisponivel",
    "CATEGORIAS": "NomeCategoria, Descricao",
    "PRODUTO_CATEGORIA": "IDCategoria, IDProduto",
    "PEDIDOS": "IDCliente, StatusPedido, ValorTotal",
    "ITEM_CATEGORIA": "IDPedido, IDProduto, Quantidade, PrecoUnitario, TotalItem"
}


def get_db_password():
    return getpass.getpass("Insira a senha para acessar o BD: ")


def sys_clear():
    # Detect the operating system
    if os.name == 'posix':  # Linux, macOS, and other POSIX systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')


def display_menu(connect: Connection):
    while True:
        sys_clear()
        print("----- SinbaExpress (ADMIN) -----")
        print("C - Inserir")
        print("R - Ler")
        print("U - Atualizar")
        print("D - Apagar")
        print("S - Sair")
        print("--------------------------------")

        choice = input("Digite sua escolha: ")

        if choice in ['C', 'c']:
            sys_clear()
            display_header(header="C")
            # Get table name from the user
            table_name = input("Digite o nome da tabela: ")
            # Get column name from the user
            column = input("Digite o nome da coluna: ")
            # Get values from the user as a comma-separated tuple
            values_input = input("Digite o(s) valore(s) como uma tupla separada por vírgula, ex:(value1,value2'): ")
            # Parse the inputs into tuples
            values = tuple(values_input.split(','))
            connect.create(
                table=table_name,
                columns=column,
                values=values
            )

        elif choice in ['R', 'r']:
            sys_clear()
            display_header(header="R")
            display_read_menu(connect=connect)

        elif choice in ['U', 'u']:
            sys_clear()
            display_header(header="U")
            # Get table name from the user
            table_name = input("Digite o nome da tabela: ")
            # Get column from the user
            column = input("Digite o nome da coluna: ")
            # Get value from the user
            value = input("Digite o valor a ser atualizado: ")
            # Get column from the user
            new_column = input("Digite o novo nome da coluna: ")
            # Get values from the user as a comma-separated tuple
            values_input = input("Digite o(s) valore(s) como uma tupla separada por vírgula, ex:(value1,value2'): ")
            # Parse the inputs into tuples
            values = tuple(values_input.split(','))
            connect.update(
                table=table_name,
                filter_column=column,
                filter_value=value,
                column_to_set=new_column,
                value_to_set=values
            )

        elif choice in ['D', 'd']:
            sys_clear()
            display_header(header='D')
            # Get table name from the user
            table_name = input("Digite o nome da tabela: ")
            # Get column from the user
            column = input("Digite o nome da coluna: ")
            # Parse the inputs into tuples
            value = input("Digite o valor a ser deletado: ")
            connect.delete(
                table=table_name,
                filter_column=column,
                filter_value=value
            )

        elif choice in ['S', 's']:
            sys_clear()
            display_header(header="S")
            # Get table name from the user
            print("Exiting the CRUD menu. Goodbye!")
            break

        else:
            sys_clear()
            print("Invalid choice. Please select a valid option.")
            input("Press any key to continue: ")


def display_header(header: str):
    sys_clear()
    print(f"------- SinbaExpress ({header}) -------")


def display_read_menu(connect: Connection):
    print("1 - Ler tudo")
    print("2 - Ler com filtro")
    print("S - Sair")
    print("--------------------------------")

    choice = input("Digite sua escolha: ")

    if choice == '1':
        sys_clear()
        display_header('R-A')
        # Get table name from the user
        table_name = input("Digite o nome da tabela: ")
        connect.read_all(table=table_name)

    elif choice == '2':
        sys_clear()
        display_header('R-F')
        # Get table name from the user
        table_name = input("Digite o nome da tabela: ")
        # Get column from the user
        column = input("Digite o nome da coluna: ")
        # Parse the inputs into tuples
        value = input("Digite o valor que deseja: ")
        # Enter the column to search
        column_to_search = input("Digite o nome da coluna que quer procurar: ")
        connect.read(
            table=table_name,
            filter_column=column,
            filter_value=value,
            columns_to_search=column_to_search
        )
    elif choice in ['S', 's']:
        sys_clear()

    else:
        sys_clear()
        print("Invalid choice. Please select a valid option.")
        input("Press any key to continue: ")


def get_table_columns(table: str):
    return table_columns[table]
