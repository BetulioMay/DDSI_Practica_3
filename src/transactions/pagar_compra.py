from interfaces.pagar_compra import get_input_data
from datetime import datetime
import cx_Oracle

# Inserta un nuevo partido en el sistema.
def pagar_compra(cursor):

    data = get_input_data()

    # Recuperamos los datos de la base de datos
    try: 
        # Obtenemos la cantidad de entradas de la base de datos
        sql = """
        select n_entradas from compra_finalizada where cod_compra = :cod_compra_introducido
        """
        c_entradas = cursor.execute(sql, cod_compra_introducido=data["cod_compra"])
        
        # Obtenemos el tipo de entrada de la base de datos
        sql = """
        select tipo_entrada from compra_finalizada where cod_compra = :cod_compra_introducido
        """
        t_entrada = cursor.execute(sql, cod_compra_introducido=data["cod_compra"])

        # Obtenemos el dni del comprador
        sql = """
        select dni from inicia where cod_compra = :cod_compra_introducido
        """
        dni = cursor.execute(sql, cod_compra_introducido=data["cod_compra"])

    except Exception as e:
        print("❌ El codigo de compra no existe en la base de datos", e)
        return False

    # Almacenamos la fecha actual
    fecha = datetime.now()

    # Calculamos el precio
    precio = 6.5*c_entradas

    try:
        ## Insertamos una nueva tupla en la tabla compra_pagada
        sql = """
        INSERT INTO compra_pagada VALUES (:cod_compra, :precio_total)
        """
        cursor.execute(sql, cod_compra=data["cod_compra"], precio_total=precio)
       
        ## Insertamos una nueva tupla en la tabla pagado. Trigger
        sql = """
        INSERT INTO paga VALUES (:cod_compra, :fecha_pago, :dni_comprador)
        """
        cursor.execute(sql, cod_compra=data["cod_compra"], fecha_pago=fecha, dni_comprador=dni)
    except Exception as e:
        print("❌ No se pudo realizar la transaccion 'Insertar partido'", e)
        return False
    
    # Mostramos la fecha de pago y el codigo de compra pagada
    print("Codigo de compra pagada: ", data["cod_compra"])
    print("Precio total: ",precio)
    return True
