from connection import Connection
from utils import *

# def display_menu(connect: Connection):
#     while True:
#         sys_clear()
#         print("\nSinbaExpress Menu:")
#         print("1. Create")
#         print("2. Read")
#         print("3. Read all")
#         print("4. Update")
#         print("5. Delete")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             sys_clear()
#             print("1. Create")
#             # Get table name from the user
#             table_name = input("Enter the table name: ")
#             # Get columns from the user as a comma-separated tuple
#             columns_input = input("Enter the columns as a comma-separated tuple (e.g.,'column1,column2'): ")
#             # Get values from the user as a comma-separated tuple
#             values_input = input("Enter the values as a comma-separated tuple (e.g.,'value1,value2'): ")
#             # Parse the inputs into tuples
#             columns = tuple(columns_input.split(','))
#             values = tuple(values_input.split(','))
#             connect.create(
#                 table=table_name,
#                 columns=columns,
#                 values=values
#             )

#         elif choice == '2':
#             sys_clear()
#             print("2. Read")
#             # Get table name from the user
#             table_name = input("Enter the table name: ")
#             # Get column from the user
#             column = input("Enter the column name: ")
#             # Parse the inputs into tuples
#             value = input("Enter the value to search: ")
#             # Enter the column to search
#             column_to_search = input("Enter the column to search name: ")
#             connect.read(
#                 table=table_name,
#                 filter_column=column,
#                 filter_value=value,
#                 columns_to_search=column_to_search
#             )

#         elif choice == '3':
#             sys_clear()
#             print("3. Read all")
#             # Get table name from the user
#             table_name = input("Enter the table name: ")
#             connect.read_all(table=table_name)

#         elif choice == '4':
#             sys_clear()
#             print("4. Update")
#             # Get table name from the user
#             table_name = input("Enter the table name: ")
#             # Get column from the user
#             column = input("Enter the column name: ")
#             # Parse the inputs into tuples
#             value = input("Enter the value to search: ")
#             # Get column from the user
#             new_column = input("Enter the new column name: ")
#             # Get values from the user as a comma-separated tuple
#             values_input = input("Enter the values to set as a comma-separated tuple (e.g.,'value1,value2'): ")
#             # Parse the inputs into tuples
#             values = tuple(values_input.split(','))
#             connect.update(
#                 table=table_name,
#                 filter_column=column,
#                 filter_value=value,
#                 column_to_set=new_column,
#                 value_to_set=values
#             )

#         elif choice == '5':
#             sys_clear()
#             print("5. Delete")
#             # Get table name from the user
#             table_name = input("Enter the table name: ")
#             # Get column from the user
#             column = input("Enter the column name: ")
#             # Parse the inputs into tuples
#             value = input("Enter the value to delete: ")
#             connect.delete(table=table_name, filter_column=column, filter_value=value)

#         elif choice == '6':
#             sys_clear()
#             print("6. Exit")
#             # Get table name from the user
#             print("Exiting the CRUD menu. Goodbye!")
#             break

#         else:
#             sys_clear()
#             print("Invalid choice. Please select a valid option.")
#             input("Press any key to continue: ")


class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = get_db_password()
        connection = Connection(db_password)

        while True:
            display_menu()
            op = input("Selecione qual operação deseja realizar: ")

            if op == "C":
                display_c_header()
                table = input("Insira o nome da tabela: ").upper()
                columns = get_table_columns(table)
                print(columns)
                values = tuple(input("Insira os valores das colunas no formato da tupla acima:\n").split(','))

                connection.create(table, columns, values)

            # if op == "R":
                # display_r_menu()
                # table = input("Insira o nome da tabela: ").upper()
                # columns = get_table_columns(table)
                # print(columns)
                # values = tuple(input("Insira os valores das colunas no formato da tupla acima:\n").split(','))

                # connection.create(table, columns, values)
