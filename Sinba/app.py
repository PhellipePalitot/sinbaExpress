from fastapi import FastAPI, HTTPException, Depends
from typing import List
import psycopg2 as db
from pydantic import BaseModel

app = FastAPI()

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

class ClienteModel(BaseModel):
    nome: str
    cpf: str
    endereco: str
    email: str
    telefone: str
    usuario: str

# Modelo Pydantic para a resposta de CREATE
class ClienteCreateResponseModel(BaseModel):
    message: str
    cliente_id: int

# Modelo Pydantic para a resposta de READ, UPDATE e DELETE
class ClienteResponseModel(BaseModel):
    message: str

# Operação CREATE (Criar um novo cliente)
@app.post("/clientes/", response_model=ClienteCreateResponseModel)
def create_cliente(cliente: ClienteModel, db: Connection = Depends(get_db)):
    try:
        sql = "INSERT INTO Clientes (Nome, CPF, Endereco, Email, Telefone, Usuario) " \
              "VALUES (%s, %s, %s, %s, %s, %s) RETURNING IDCliente"
        db.execute(sql, (cliente.nome, cliente.cpf, cliente.endereco, cliente.email, cliente.telefone, cliente.usuario))
        cliente_id = db.cur.fetchone()[0]
        db.commit()
        return {"message": "Cliente criado com sucesso", "cliente_id": cliente_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente: {str(e)}")

# Operação READ (Ler informações de um cliente)
@app.get("/clientes/{cliente_id}/", response_model=ClienteModel)
def read_cliente(cliente_id: int, db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Clientes WHERE IDCliente = %s"
        db.execute(sql, (cliente_id,))
        result = db.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        
        # Transforma o resultado em uma instância de ClienteModel
        cliente = ClienteModel(
            nome=result[0][1],
            cpf=result[0][2],
            endereco=result[0][3],
            email=result[0][4],
            telefone=result[0][5],
            usuario=result[0][6]
        )

        return cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler cliente: {str(e)}")


# Operação UPDATE (Atualizar as informações de um cliente)
@app.put("/clientes/{cliente_id}/", response_model=ClienteResponseModel)
def update_cliente(cliente_id: int, cliente: ClienteModel, db: Connection = Depends(get_db)):
    try:
        sql = "UPDATE Clientes SET Nome=%s, CPF=%s, Endereco=%s, Email=%s, Telefone=%s, Usuario=%s WHERE IDCliente=%s"
        db.execute(sql, (cliente.nome, cliente.cpf, cliente.endereco, cliente.email, cliente.telefone, cliente.usuario, cliente_id))
        db.commit()
        return {"message": "Cliente atualizado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar cliente: {str(e)}")

# Operação DELETE (Excluir um cliente)
@app.delete("/clientes/{cliente_id}/", response_model=ClienteResponseModel)
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
@app.get("/clientes/", response_model=List[ClienteModel])
def read_all_clientes(db: Connection = Depends(get_db)):
    try:
        sql = "SELECT * FROM Clientes"
        db.execute(sql)
        results = db.fetchall()

        # Transforma os resultados em uma lista de instâncias de ClienteModel
        clientes = [{"IDCliente": row[0], "nome": row[1], "cpf": row[2], "endereco": row[3], "email": row[4], "telefone": row[5], "usuario": row[6]} for row in results]

        return clientes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler todos os clientes: {str(e)}")
