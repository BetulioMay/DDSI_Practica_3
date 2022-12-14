'''
Funciones de utilidad con transacciones
'''

def check_stock(cursor, product_id, quantity):
	sql = '''
	SELECT cantidad FROM stock WHERE cproducto = :prodid
	'''
	cursor.execute(sql, prodid=product_id)
	result = cursor.fetchone()
	if result is None:
		print(f">> ERROR: No se encontro un producto con codigo {product_id}.")
		return False

	avail_quantity = result[0]
	if quantity > avail_quantity:
		print(f">> ERROR: no hay suficiente stock para el producto {product_id}.")
		return False
	
	return True

def check_order_id(cursor, order_id):
	sql = '''
	SELECT * FROM pedido WHERE Cpedido = :ordid
	'''
	cursor.execute(sql, ordid=order_id)

	if cursor.fetchone() != None:
		print(f"El pedido {order_id} ya existe.")
		return False
	return True