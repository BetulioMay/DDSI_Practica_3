import constants as c

def main_menu():
	print(c.HEADER)
	print("MENU PRINCIPAL")
	print("Selecciona una opcion:")
	print("1. Crear tablas")
	print("2. Borrar tablas")
	print("3. Dar de alta pedido")
	print("4. Mostrar tablas")
	print("5. Salir")
	option = input(c.IN_PROMPT)
	
	# Devolvemos cero como opcion nula
	return int(option) if option.isdigit() else 0