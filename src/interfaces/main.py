import constants as c


def main_menu():
    print(c.HEADER)
    print("MENU PRINCIPAL")
    print("Selecciona una opcion:")
    print("1. Parejas entrenador")
    print("2. Pagar compra")
    print("3. Guardar partido")
    print("4. Salir")
    option = input(c.IN_PROMPT)

    # Devolvemos cero como opcion nula
    return int(option) if option.isdigit() else 0
