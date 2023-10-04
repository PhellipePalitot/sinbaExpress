import os
import getpass

table_columns = {
    "CLIENTES": "Nome, CPF, Endereco, Email, Telefone, Usuario",
    "PRODUTOS": "NomeProduto, Descricao, Preco, EstoqueDisponivel",
    "CATEGORIAS": "NomeCategoria, Descricao",
    "PRODUTO_CATEGORIA": "IDCategoria, IDProduto",
    "PEDIDOS": "IDCliente, StatusPedido, ValorTotal",
    "ITEM_CATEGORIA": "IDPedido, IDProduto, Quantidade, PrecoUnitario, TotalItem"
}

def get_db_password():
    db_password = getpass.getpass("Insira a senha para acessar o BD: ")
    return db_password

def sys_clear():
    # Detect the operating system
    if os.name == 'posix':  # Linux, macOS, and other POSIX systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def display_menu():
    sys_clear()
    print("----- SinbaExpress (ADMIN) -----")
    print("C - Inserir")
    print("R - Ler")
    print("U - Atualizar")
    print("D - Apagar")
    print("S - Sair")
    print("--------------------------------")

def display_c_header():
    sys_clear()
    print("------- SinbaExpress (C) -------")

def get_table_columns(table: str):
    return table_columns[table]