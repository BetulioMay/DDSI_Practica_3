
from datetime import datetime
import constants as c

def get_order_data():
	print(c.HEADER)
	
	# NOTE: La insercion de un codigo de pedido es solo para testear
	# se pretende generar identificadores unicos para los pedidos.
	order_id = ''
	client_id = ''
	while order_id == '' or order_id is None and order_id.isdigit():
		print("Introduzca el codigo del pedido")
		order_id = input(c.IN_PROMPT)
	while client_id == '' or client_id is None and client_id.isdigit():
		print("Introduzca su codigo de cliente")
		client_id = input(c.IN_PROMPT)
	order_date = datetime.now()
	return int(order_id), client_id, order_date

def order_menu():
	print(c.HEADER)
	print("MENU PEDIDO")
	print("Selecciona una opcion:")
	print("1. Añadir detalle de producto")
	print("2. Eliminar todos los detalles de producto")
	print("3. Cancelar pedido")
	print("4. Finalizar pedido")
	option = input(c.IN_PROMPT)
	
	# Devolvemos 0 como opcion nula
	return int(option) if option.isdigit() else 0