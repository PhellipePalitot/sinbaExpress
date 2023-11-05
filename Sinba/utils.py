import getpass
import os

table_columns = {
    "CLIENTES": "Nome, CPF, Endereco, Email, Telefone, Usuario",
    "PRODUTOS": "NomeProduto, Descricao, Preco, EstoqueDisponivel",
    "CATEGORIAS": "NomeCategoria, Descricao",
    "PRODUTO_CATEGORIA": "IDCategoria, IDProduto",
    "PEDIDOS": "IDCliente, StatusPedido, ValorTotal",
    "ITEM_CATEGORIA": "IDPedido, IDProduto, Quantidade, PrecoUnitario, TotalItem"
}

def get_table_columns(table: str):
    return table_columns[table]

def sys_clear():
    if os.name == 'posix':  # Linux, macOS, and other POSIX systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def get_db_password():
    sys_clear()
    return getpass.getpass("Insira a senha para acessar o BD: ")

def display_header(header: str):
    sys_clear()
    print(f"------- SinbaExpress ({header}) -------")

def display_menu():
    sys_clear()
    print("----- SinbaExpress (ADMIN) -----")
    print("C   - Inserir")
    print("R   - Ler")
    print("U   - Atualizar")
    print("D   - Apagar")
    print("S   - Sair")
    print("RLP - Relatório de Produtos")
    print("--------------------------------")

def display_read_options():
    print("1 - Ler tudo")
    print("2 - Ler com filtro")
    print("S - Sair")
    print("--------------------------------")
