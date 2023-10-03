from connection import Connection
import getpass

class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = getpass.getpass("Enter the password to access the DB: ")
        connection = Connection(db_password)
        print(connection.read_all("Clientes"))
        return
