#!/usr/bin/env python3

"""
Programa principal.
Aqui se ejecutara el `main loop` del programa
"""

from dotenv import load_dotenv

load_dotenv()

import connection
import interfaces.main as main
from constants import MENU_OPTION
import transactions.register_order as register_order
from transactions.drop_insert import drop_tables, create_tables, insert_stock
from transactions.show_tables import show_tables
from transactions.partido import insert_partido


def run():
    conn = connection.connect()
    cursor = connection.get_cursor(conn)

    finish = False
    option = None
    while not finish:
        option = main.main_menu()
        match option:
            case MENU_OPTION.CREATE_TABLES.value:
                # TODO: Crear otro insert `insert_tables` donde se inserten los datos
                # que se necesiten, en vez de insert_stock (codigo viejo)
                if create_tables(cursor=cursor) and insert_stock(cursor=cursor):
                    print("Tablas creadas.")
                    connection.commit(conn)
                else:
                    print("No se han conseguido crear el stock.")
            case MENU_OPTION.DROP_TABLES.value:
                if drop_tables(cursor=cursor):
                    print("Tablas borradas")
                    connection.commit(conn)
                else:
                    print("No se han conseguido borrar las tablas")
            case MENU_OPTION.PAREJAS_ENTRENADOR.value:
                # TODO: Implementar funcion que muestre las tablas de las parejas
                # que un entrenador entrena en una edicion (RF1.4)
                print("Not implemented.")
            case MENU_OPTION.PAGAR_COMPRA.value:
                # TODO: Implementar funcion de insertar una nueva compra pagada (RF2.4)
                print("Not implemented.")
            case MENU_OPTION.GUARDAR_PARTIDO.value:
                # TODO: Testear esta transaccion (RF3.1)
                if not insert_partido(cursor=cursor):
                    print("⏪ Rolling back...")
                    connection.rollback(conn=conn)
                else:
                    connection.commit(conn=conn)
                    print("✅ Se ha guardado el partido correctamente")
            case MENU_OPTION.EXIT_MENU.value:
                print("🔌 Cerrando conexion...")
                connection.close_cursor(cursor=cursor)
                connection.close_connection(conn=conn)
                print("👋🏼 BYE.")
                finish = True


if __name__ == "__main__":
    run()
