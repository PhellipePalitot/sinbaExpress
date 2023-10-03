from connection import Connection
import os
import getpass


def sys_clear():
    # Detect the operating system
    if os.name == 'posix':  # Linux, macOS, and other POSIX systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')


def display_menu(connect: Connection):
    while True:
        sys_clear()
        print("\nSinbaExpress Menu:")
        print("1. Create")
        print("2. Read")
        print("3. Read all")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            # Get columns from the user as a comma-separated tuple
            columns_input = input("Enter the columns as a comma-separated tuple (e.g.,'column1,column2'): ")
            # Get values from the user as a comma-separated tuple
            values_input = input("Enter the values as a comma-separated tuple (e.g.,'value1,value2'): ")
            # Parse the inputs into tuples
            columns = tuple(columns_input.split(','))
            values = tuple(values_input.split(','))
            connect.create(
                table=table_name,
                columns=columns,
                values=values
            )

        elif choice == '2':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            # Get column from the user
            column = input("Enter the column name: ")
            # Get values from the user as a comma-separated tuple
            values_input = input("Enter the values as a comma-separated tuple (e.g.,'value1,value2'): ")
            # Enter the column to search
            column_to_search = input("Enter the column to search name: ")
            # Parse the inputs into tuples
            values = tuple(values_input.split(','))
            connect.read(
                table=table_name,
                filter_column=column,
                filter_value=values,
                columns_to_search=column_to_search
            )

        elif choice == '3':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            connect.read_all(table=table_name)

        elif choice == '4':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            connect.update(table=table_name, filter_column=, filter_value=,column_to_set=, value_to_set=)

        elif choice == '5':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            connect.delete(table=table_name, filter_column=, filter_value=)

        elif choice == '6':
            sys_clear()
            # Get table name from the user
            table_name = input("Enter the table name: ")
            print("Exiting the CRUD menu. Goodbye!")
            break

        else:
            sys_clear()
            print("Invalid choice. Please select a valid option.")
            input("Press any key to continue: ")


class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = getpass.getpass("Enter the password to access the DB: ")
        connection = Connection(db_password)
        display_menu(connect=connection)
        print(connection.read_all("Clientes"))
        return
