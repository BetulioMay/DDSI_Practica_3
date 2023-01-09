from datetime import datetime
import constants as c


def get_input_data():
    print(c.HEADER)

    # NOTE: Segun el requisito funcional, `cod_partido` no es
    #       un dato de entrada. Sin embargo, por motivos de simplicidad
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
    data["cod_partido"] = int(data["cod_partido"])

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
            if (
                len(dni) == 9
                and not dni[len(dni) - 1].isdigit()
                # Solo hay una letra. El ultimo simbolo.
                and len([x for x in dni if not x.isdigit()]) == 1
            ):
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
    data["num_pista"] = int(data["num_pista"])

    while (
        data["cod_edicion"] == ""
        or data["cod_edicion"] == None
        or not data["cod_edicion"].isdigit()
    ):
        print("Introduzca el codigo de edicion")
        data["cod_edicion"] = input(c.IN_PROMPT)
    data["cod_edicion"] = int(data["cod_edicion"])

    # Tomamos la fecha actual
    print("Introduzca la fecha del partido ('DD/MM/YY HH:MM:SS')")
    strdate = input("(DEFAULT toma la fecha actual)" + c.IN_PROMPT)
    if len(strdate) > 0:
        data["fecha"] = datetime.strptime(strdate, "%d/%m/%y %H:%M:%S")
    else:
        data["fecha"] = datetime.now()

    return data
