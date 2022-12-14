
import interfaces.order as order
import interfaces.detail_order as detail
from transactions.helpers import check_stock, check_order_id
from constants import ORDER_OPTION
from connection import commit, rollback, savepoint, rollback_to
from transactions.show_tables import show_tables

# Inserta un nuevo pedido a la tabla Pedido
def insert_basic_data(cursor):
	order_id, client_id, order_date = order.get_order_data()

	if not check_order_id(cursor, order_id):
		print("Cancelando pedido...")
		return None

	sql = '''
		INSERT INTO pedido VALUES (:ordid, :clid, :orddt)
	'''
	cursor.execute(sql, ordid=order_id, clid=client_id, orddt=order_date)

	return order_id

# Inserta un detalle de un pedido a la tabla Detalle-Pedido
def insert_order_detail(cursor, order_id):
	# Pedir al usuario los datos del detalle de pedido
	product_id, quantity = detail.get_detail_data()

	# Chequear que hay stock para el pedido con la cantidad deseada
	result = check_stock(cursor, product_id, quantity)
	if not result:
		print("Cancelando detalle de pedido...")
		return False

	# En caso de haber stock insertar el detalle de pedido y actualizar stock
	sql = '''
	INSERT INTO detalle_pedido VALUES (:ordid, :prodid, :quan)
	'''
	cursor.execute(sql, ordid=order_id, prodid=product_id, quan=quantity)

	sql = '''
	UPDATE stock SET cantidad = cantidad - :quan WHERE Cproducto = :prodid
	'''
	cursor.execute(sql, prodid=product_id, quan=quantity)
	return True

# Registra o da de alta un nuevo pedido
def register_order(conn, cursor):
	'''
	Schema:
		Stock(PK Cproducto, cantidad)
		Pedido(PK Cpedido, Ccliente, Fecha_pedido)
		Detalle-Pedido(FK Cpedido, FK Cproducto, Cantidad), PK(Cpedido, Cproducto)
	'''
	order_id = insert_basic_data(cursor=cursor)
	if order_id == None:
		return
	# Cuando inserte los datos visualizar la DB
	show_tables(cursor)

	svpt = "insert_order"
	savepoint(cursor, svpt)

	end_transaction = False
	option = None
	while not end_transaction:
		option = order.order_menu()
		match option:
			case ORDER_OPTION.ADD_DETAIL.value:
				if insert_order_detail(cursor, order_id): print("Se ha añadido un detalle de pedido.")
				else: print("No se ha añadido ningun detalle de pedido.")
				show_tables(cursor=cursor)
			case ORDER_OPTION.DELETE_DETAILS.value:
				print("Borrando detalles del pedido...")
				rollback_to(cursor, svpt)
				show_tables(cursor=cursor)
			case ORDER_OPTION.CANCEL_ORDER.value:
				print("Cancelando pedido...")
				rollback(conn)
				end_transaction = True
				show_tables(cursor=cursor)
			case ORDER_OPTION.FINISH_ORDER.value:
				print("Guardando cambios...")
				commit(conn)
				print("Hecho.")
				end_transaction = True
				