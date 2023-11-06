from fastapi import FastAPI, HTTPException, Depends
from typing import List
import psycopg2 as db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Substitua pela origem do seu aplicativo React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Connection class for interacting with the PostgreSQL database
class Connection:
    def __init__(self, db_password):
        self.postgres = {
            "host": "172.17.0.3",
            "port": "5432",
            "user": "postgres",
            "password": db_password,
            "database": "postgres"
        }

        try:
            self.conn = db.connect(**self.postgres)
            self.cur = self.conn.cursor()
        except Exception as error:
            print("Error connecting to PostgreSQL database:", error)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def commit(self):
        return self.conn.commit()

    def fetchall(self):
        return self.cur.fetchall()

    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cur.execute(str(sql), params or ())
        return self.fetchall()

# Function to get the database connection
def get_db():
    db_connection = Connection(db_password='senha123')  # Replace with your actual db password
    yield db_connection
    db_connection.conn.close()

# Operação CREATE (Criar um novo cliente)
@app.post("/clientes/", response_model=dict)
def create_cliente(cliente: dict, db: Connection = Depends(get_db)):
    try:
        sql = "INSERT INTO Clientes (Nome, CPF, Endereco, Email, Telefone, Usuario) " \
              "VALUES (%s, %s, %s, %s, %s, %s) RETURNING IDCliente"
        db.execute(sql, (cliente["nome"], cliente["cpf"], cliente["endereco"], cliente["email"], cliente["telefone"], cliente["usuario"]))
        cliente_id = db.cur.fetchone()[0]
        db.commit()

        return {"message": "Cliente criado com sucesso", "cliente_id": cliente_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente: {str(e)}")

# Operação READ (Ler informações de um cliente)
@app.get("/clientes/{cliente_id}/", response_model=List[dict])
def read_cliente(cliente_id: int, db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Clientes WHERE IDCliente = %s"
        db.execute(sql, (cliente_id,))
        result = db.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        
        cliente = [{"nome":row[1], "cpf":row[2], "endereco":row[3], "email":row[4], "email":row[5], "email":row[6]} for row in result]
        return cliente

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler cliente: {str(e)}")


# Operação UPDATE (Atualizar as informações de um cliente)
@app.put("/clientes/{cliente_id}/", response_model=dict)
def update_cliente(cliente_id: int, cliente: dict, db: Connection = Depends(get_db)):
    try:
        sql = "UPDATE Clientes SET Nome=%s, CPF=%s, Endereco=%s, Email=%s, Telefone=%s, Usuario=%s WHERE IDCliente=%s"
        db.execute(sql, (cliente["nome"], cliente["cpf"], cliente["endereco"], cliente["email"], cliente["telefone"], cliente["usuario"], cliente_id))
        db.commit()
        return {"message": "Cliente atualizado com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar cliente: {str(e)}")

# Operação DELETE (Excluir um cliente)
@app.delete("/clientes/{cliente_id}/", response_model=dict)
def delete_cliente(cliente_id: int, db: Connection = Depends(get_db)):
    try:
        sql = "DELETE FROM Clientes WHERE IDCliente = %s RETURNING IDCliente"
        db.execute(sql, (cliente_id,))
        cliente_id = db.cur.fetchone()[0]
        db.commit()
        return {"message": "Cliente excluído com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir cliente: {str(e)}")

# Operação READ ALL (Ler todas as informações dos clientes)
@app.get("/clientes/", response_model=List[dict])
def read_all_clientes(db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Clientes"
        results = db.query(sql)

        clientes = [{"IDCliente": row[0], "nome": row[1], "cpf": row[2], "endereco": row[3], "email": row[4], "telefone": row[5], "usuario": row[6]} for row in results]
        return clientes

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler todos os clientes: {str(e)}")

# Operação READ (Ler as informações de um produto)
@app.get("/produtos/{produto_id}/", response_model=List[dict])
def read_produto(produto_id: int, db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Produtos WHERE IDProduto = %s"
        result = db.query(sql, (produto_id,))
        if not result:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        produto = [{"nome_produto":row[1], "descricao":row[2], "preco":row[3], "estoque_disponivel":row[4]} for row in result]
        return produto

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler produto: {str(e)}")

# Operação UPDATE (Atualizar as informações de um produto)
@app.put("/produtos/{produto_id}/", response_model=dict)
def update_produto(produto_id: int, produto: dict, db: Connection = Depends(get_db)):
    try:
        sql = "UPDATE Produtos SET NomeProduto=%s, Descricao=%s, Preco=%s, EstoqueDisponivel=%s WHERE IDProduto=%s"
        db.execute(sql, (produto.nome_produto, produto.descricao, produto.preco, produto.estoque_disponivel, produto_id))
        db.commit()
        return {"message": "Produto atualizado com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar produto: {str(e)}")

# Operação DELETE (Excluir um produto)
@app.delete("/produtos/{produto_id}/", response_model=dict)
def delete_produto(produto_id: int, db: Connection = Depends(get_db)):
    try:
        sql = "DELETE FROM Produtos WHERE IDProduto = %s RETURNING IDProduto"
        db.execute(sql, (produto_id,))
        produto_id = db.cur.fetchone()[0]
        db.commit()

        return {"message": "Produto excluído com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir produto: {str(e)}")

# Operação READ ALL (Ler todas as informações dos produtos)
@app.get("/produtos/", response_model=List[dict])
def read_all_produtos(db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Produtos"
        results = db.query(sql)

        produtos = [{"IDProduto": row[0], "nome_produto": row[1], "descricao": row[2], "preco": float(row[3]), "estoque_disponivel": row[4]} for row in results]
        return produtos

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler todos os produtos: {str(e)}")

@app.put("/procedure/estoque/{categoria_id}/{qnt}", response_model=dict)
def abastecer_estoque(categoria_id: int, qnt: int, db: Connection = Depends(get_db)):
    try:
        sql_1 = "CREATE OR REPLACE PROCEDURE ReabastecerProdutosSemEstoque (p_quantidade_a_adicionar INT, p_categoria_id INT) "
        sql_2 = "LANGUAGE SQL "
        sql_3 = "BEGIN ATOMIC "
        sql_4 = "UPDATE Produtos p SET EstoqueDisponivel = p.EstoqueDisponivel + p_quantidade_a_adicionar "
        sql_5 = "FROM Produto_Categoria pc WHERE pc.IDProduto = p.IDProduto "
        sql_6 = "AND pc.IDCategoria = p_categoria_id AND p.EstoqueDisponivel = 0; "
        sql_7 = "END; "
        sql_8 = "CALL ReabastecerProdutosSemEstoque(%s, %s)"
        sql = sql_1+sql_2+sql_3+sql_4+sql_5+sql_6+sql_7+sql_8

        db.execute(sql, (qnt, categoria_id))
        db.commit()

        return {"message": "Categoria abastecida com sucesso"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

@app.get("/view/produtos/", response_model=dict)
def view_produtos(db: Connection = Depends(get_db)):
    try:
        sql_1 = "CREATE OR REPLACE VIEW Produto_Categoria_View AS "
        sql_2 = "SELECT p.NomeProduto, p.Descricao, p.Preco, c.NomeCategoria AS Categoria "
        sql_3 = "FROM Produtos p JOIN Produto_Categoria pc ON p.IDProduto = pc.IDProduto "
        sql_4 = "JOIN Categorias c ON pc.IDCategoria = c.IDCategoria; "
        sql_5 = "SELECT * FROM Produto_Categoria_View"
        sql = sql_1+sql_2+sql_3+sql_4+sql_5

        result = db.query(sql)

        if not result:
            raise HTTPException(status_code=404, detail="Nenhum produto cadastrado")

        view = [{"nome_produto": row[0], "descricao": row[1], "preco": row[2], "categoria": row[3]} for row in result]
        return view

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

# Operação finalizar compra (Atualiza o estoque dos produtos)
@app.put("/finalizar/{client_id}", response_model=dict)
def finaliza_compra(client_id: int, produtos: dict, db: Connection = Depends(get_db)):
    try:
        pedido = {}
        for p in produtos:
            id = p["IDProduto"]
            estoque = p["estoque_disponivel"]

            if id not in pedido:
                pedido[id] = {"qnt_compra": 0, "estoque_atual": estoque, "novo_estoque": estoque}

            pedido[id]["qnt_compra"] += 1
            pedido[id]["novo_estoque"] -= 1
            if pedido[id]["novo_estoque"] < 0:
                raise HTTPException(status_code=400, detail=f"Estoque esgotado para o produto {id}.")

        for (id_produto, values) in pedido.items():
            sql_update = "UPDATE Produtos SET EstoqueDisponivel=%s WHERE IDProduto=%s"
            db.execute(sql_update, (values["novo_estoque"], id_produto))
            db.commit()
            return {"message": "Compra realizada!"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Não foi possível atualizar o estoque: {str(e)}")
