import constants as c

def get_input_data():
    print(c.HEADER)

    data = {
        "dni_entre" : "",
        "cod_edicion" : "",
    }

    bien = False

    while (not bien):
        print(
            "Introduzca el DNI del entrenador"
        )
        data["dni_entre"] = input(c.IN_PROMPT)
        # Chequear la validez del DNI. No lo puede hacer el SGBD.
        if (
            len(data["dni_entre"]) == 9
            and not data["dni_entre"][len(data["dni_entre"]) - 1].isdigit()
            # Solo hay una letra. El ultimo simbolo.
            and len([x for x in data["dni_entre"] if not x.isdigit()]) == 1
        ):
            bien = True
        else:
            print(f"DNI invalido. Introduzca los datos de nuevo.")

    while (
        data["cod_edicion"] == ""
        or data["cod_edicion"] == None
        or not data["cod_edicion"].isdigit()
    ):
        print("Introduzca el codigo de edicion")
        data["cod_edicion"] = input(c.IN_PROMPT)

    data["cod_edicion"] = int(data["cod_edicion"])

    return data