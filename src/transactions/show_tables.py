from interfaces.show_tables import get_input_data
import cx_Oracle
import constants as c

def show_tables(cursor):
	try:
		print("\n\tTabla stock")
		print("Cproducto \t cantidad")
		print("---------------------------------")
		for row in cursor.execute("select * from stock"):
			print(f"| \t{row[0]} \t| \t{row[1]} \t|")
		print("---------------------------------\n")

		print("\t\tTabla pedido")
		print("Cpedido \t Ccliente \t fecha_pedido")
		print("---------------------------------------------------------")
		for row in cursor.execute("select * from pedido"):
			print(f"| \t{row[0]} \t| \t{row[1]} \t| \t{row[2].year}/{row[2].month}/{row[2].day} \t|")
		print("---------------------------------------------------------\n")

		print("\t\tTabla detalle_pedido")
		print("Cpedido \t Cproducto \t cantidad")
		print("-------------------------------------------------")
		for row in cursor.execute("select * from detalle_pedido"):
			print(f"| \t{row[0]} \t| \t{row[1]} \t| \t{row[2]} \t|")
		print("-------------------------------------------------\n")
	except:
		print("Tablas no creadas.")
		return

def parejas_entrenador(cursor):
	data = get_input_data()

	try:
		DNI_1 = []
		DNI_2 = []

		for row in cursor.execute("select * from entrena"):
			if (row[0] == data["dni_entre"] and row[3] == data["cod_edicion"]):
				DNI_1.append(row[1])
				DNI_2.append(row[2])
		
		contador = 1
		i = 0
		if (len(DNI_1) != 0):
			print("\nParejas entrenadas:")
			for row in cursor.execute("select * from jugador"):
				if (len(DNI_1) > 1):
					for dni, dni2 in DNI_1, DNI_2:
						if (row[0] == dni or row[0] == dni2):
							if (i % 2 == 0):
								print(c.HEADER)
								print(f"Pareja nº: {contador}")
								contador += 1
							print(f"Nombre: {row[1]}, Apellidos: {row[2]}")
							i += 1
				else:
					if (row[0] == DNI_1[0] or row[0] == DNI_2[0]):
							if (i % 2 == 0):
								print(c.HEADER)
								print(f"Pareja nº: {contador}")
								contador += 1
							print(f"Nombre: {row[1]}, Apellidos: {row[2]}")
							i += 1
						
		else:
			print("El entrenador no tiene asignada ninguna pareja")

	except:
		print("No se pudo ejecutar la orden")
		return
