from utils import *


class SinbaExpress():
    def __init__(self):
        return

    def iniciar(self):
        db_password = get_db_password()
        connection = Connection(db_password)
        display_menu(connect=connection)