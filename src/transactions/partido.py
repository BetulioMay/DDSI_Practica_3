from interfaces.partido import get_input_data
import cx_Oracle

# Inserta un nuevo partido en el sistema.
def insert_partido(cursor):

    data = get_input_data()

    try:
        ## Insertamos el partido para integridad referencial (cod_partido)
        sql = """
        INSERT INTO partido VALUES (:cod_partido, :fecha)
        """
        cursor.execute(sql, cod_partido=data["cod_partido"], fecha=data["fecha"])

        ## Insertamos en `hospeda`
        sql = """
        INSERT INTO hospeda VALUES (:codedi, :codpar)
        """
        cursor.execute(sql, codedi=data["cod_edicion"], codpar=data["cod_partido"])

        ## Insertamos en `juegan`
        sql = """
        INSERT INTO juegan VALUES (:codpar, :dni1_1, :dni1_2, :dni2_1, :dni2_2)
        """
        cursor.execute(
            sql,
            codpar=data["cod_partido"],
            dni1_1=data["dnis"][0],
            dni1_2=data["dnis"][1],
            dni2_1=data["dnis"][2],
            dni2_2=data["dnis"][3],
        )

        # Insertamos en `se_juega_en`. TRIGGER
        sql = """
        INSERT INTO se_juega_en VALUES (:numpis, :codpar)
        """
        cursor.execute(sql, numpis=data["num_pista"], codpar=data["cod_partido"])

        # Insertamos en `arbitra`
        sql = """
        INSERT INTO arbitra VALUES (:dniarb, :codpar)
        """
        cursor.execute(
            sql, dniarb=data["dnis"][len(data["dnis"] - 1)], codpar=data["cod_partido"]
        )

    except Exception as e:
        print("No se pudo realizar la transaccion 'Insertar partido'", e)
        return False

    return True
