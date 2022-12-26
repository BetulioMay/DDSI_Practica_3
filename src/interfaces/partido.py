from datetime import datetime
import constants as c


def get_input_data():
    print(c.HEADER)

    # NOTE: Segun el requisito funcional, `cod_partido` no es
    #       un dato de entrada. Sin embargo, por motivos de sencillez
    #       se lo pedimos al usuario.

    # Pedir al usuario estos datos
    data = {
        "cod_partido": "",
        "dnis": [],
        "num_pista": "",
        "cod_edicion": "",
        "fecha": None,
    }

    while (
        data["cod_partido"] == ""
        or data["cod_partido"] == None
        or not data["cod_partido"].isdigit()
    ):
        print("Introduzca el codigo de partido")
        data["cod_partido"] = input(c.IN_PROMPT)
    while len(data["dnis"]) != 5:
        # Reset la lista de dnis
        data["dnis"].clear()

        print(
            "Introduzca los dnis de los jugadores y del arbitro separado por espacios (j1_1 j1_2 j2_1 j2_2 arb)"
        )
        dnis = input(c.IN_PROMPT)
        dnis = dnis.split(sep=" ")
        for dni in dnis:
            # Chequear la validez de los DNIs. No lo puede hacer el SGBD.
            if len(dni) == 9 and dni[len(dni) - 1].isdigit():
                data["dnis"].append(dni)
            else:
                print(f"DNI {dni} invalido. Introduzca los datos de nuevo.")
                data["dnis"].clear()
                break

    while (
        data["num_pista"] == ""
        or data["num_pista"] == None
        or not data["num_pista"].isdigit()
    ):
        print("Introduzca el numero de pista")
        data["num_pista"] = input(c.IN_PROMPT)

    while (
        data["cod_edicion"] == ""
        or data["cod_edicion"] == None
        or not data["cod_edicion"].isdigit()
    ):
        print("Introduzca el codigo de edicion")
        data["cod_edicion"] = input(c.IN_PROMPT)

    # Tomamos la fecha actual
    data["fecha"] = datetime.now()
    return data
