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
from transactions.partido import insert_partido
from transactions.pagar_compra import pagar_compra
from transactions.show_tables import parejas_entrenador


def run():
    conn = connection.connect()
    cursor = connection.get_cursor(conn)

    finish = False
    option = None
    while not finish:
        option = main.main_menu()
        match option:
            case MENU_OPTION.PAREJAS_ENTRENADOR.value:
                # TODO: Implementar funcion que muestre las tablas de las parejas
                # que un entrenador entrena en una edicion (RF1.4)
                parejas_entrenador(cursor=cursor)
            case MENU_OPTION.PAGAR_COMPRA.value:
                if not pagar_compra(cursor=cursor):
                    print("⏪ Rolling back...")
                    connection.rollback(conn=conn)
                else:
                    connection.commit(conn=conn)
                    print("✅ Se ha guardado el pago correctamente")
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
