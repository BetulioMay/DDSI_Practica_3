import constants as c

def get_detail_data():
	print(c.HEADER)
	product_id = ''
	while product_id == '':
		print("Introduzca el codigo de producto")
		product_id = input(c.IN_PROMPT)
	quantity = ''
	while quantity == '':
		print("Introduzca la cantidad deseada")
		quantity = input(c.IN_PROMPT)
	return int(product_id), int(quantity)