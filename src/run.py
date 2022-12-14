#!/usr/bin/env python3

'''
Programa principal.
Aqui se ejecutara el `main loop` del programa
'''

from dotenv import load_dotenv
load_dotenv()

import connection
import interfaces.main as main
from constants import MENU_OPTION
import transactions.register_order as register_order
from transactions.drop_insert import drop_tables, create_tables, insert_stock
from transactions.show_tables import show_tables

def run():
	conn = connection.connect()
	cursor = connection.get_cursor(conn)

	finish = False
	option = None
	while not finish:
		option = main.main_menu()
		match option:
			case MENU_OPTION.CREATE_TABLE.value:
				if create_tables(cursor=cursor) and insert_stock(cursor=cursor):
					print("Stock creado.")
					connection.commit(conn)
				else:
					print("No se han conseguido crear el stock.")
			case MENU_OPTION.DROP_TABLE.value:
				if drop_tables(cursor=cursor):
					print("Tablas borradas")
					connection.commit(conn)
				else:
					print("No se han conseguido borrar las tablas")				
			case MENU_OPTION.REGISTER_ORDER.value:
				register_order.register_order(conn=conn, cursor=cursor)
			case MENU_OPTION.SHOW_TABLES.value:
				show_tables(cursor=cursor)
			case MENU_OPTION.EXIT_MENU.value:
				connection.close_cursor(cursor=cursor)
				connection.close_connection(conn=conn)
				print("BYE.")
				finish = True

if __name__ == "__main__":
	run()

