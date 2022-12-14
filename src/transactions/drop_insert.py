
def drop_tables(cursor) :
  drop_details = "drop table detalle_pedido"
  drop_order = "drop table pedido"
  drop_stock = "drop table stock"
  try:
      cursor.execute(drop_details)
      cursor.execute(drop_order)
      cursor.execute(drop_stock)
  except Exception as e: 
      print(e)
      return False
  return True

def insert_stock(cursor):
	data = [
		(1, 10),
		(2, 24),
    (3, 33),
    (4, 4),
    (5, 56),
    (6, 29),
    (7, 15),
    (8, 9),
    (9, 60),
    (10, 3)
	]
	try:
		sql = '''
		INSERT INTO stock VALUES (:1, :2)
		'''
		cursor.executemany(sql, data)
	except Exception as e:
		print(e)
		return False
	return True

def create_tables(cursor) :
	insert_stock = "create table stock (Cproducto int not null primary key,cantidad int default 0)"
	insert_order = "create table pedido (Cpedido int not null primary key,Ccliente int not null,fecha_pedido date)"
	insert_details = "create table detalle_pedido (Cpedido references pedido(Cpedido),Cproducto references stock(Cproducto),cantidad int default 1,primary key (Cpedido, Cproducto))"
	try:
		cursor.execute(insert_stock)
		cursor.execute(insert_order)
		cursor.execute(insert_details)
	except Exception as e: 
		print(e)
		return False
	return True
