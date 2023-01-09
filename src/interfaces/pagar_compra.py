import constants as c

def get_input_data():
    print(c.HEADER)

    # Pedimos al usuario los datos necesarios 
    data = {
        "cod_compra": "",
    }

    #Comprobamos que introduce un valor correcto
    while (
        data["cod_compra"] == ""
        or data["cod_compra"] == None
        or len(data["cod_compra"]) > 15
    ):
        print("Introduzca el codigo de compra finalizada")
        data["cod_compra"] = input(c.IN_PROMPT)
    
    return data
