from connection import Connection
import getpass


def display_menu(connect: Connection):
    while True:
        print("\nSinbaExpress Menu:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            connect.create()
        elif choice == '2':
            connect.read()
        elif choice == '3':
            connect.update()
        elif choice == '4':
            connect.delete()
        elif choice == '5':
            print("Exiting the CRUD menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = getpass.getpass("Enter the password to access the DB: ")
        connection = Connection(db_password)
        display_menu(connect=connection)
        print(connection.read_all("Clientes"))
        return
