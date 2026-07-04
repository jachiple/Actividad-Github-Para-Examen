#MODULO !!!



def validar_codigo(codigo, productos):
    cod = codigo.strip().upper()
    if cod == "":
        return False
    if cod in productos:
        return False
    return True

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False


def validar_stock(stock):
    try:
        val = int(stock)
        return val >= 0
    except ValueError:
        return False

def 











def leer_opcion():
    try:
        opcionmod = int(input("Seleccione una opción: "))
        if 1 <= opcionmod <= 7:
            return opcionmod
        else:
            return -1
    except ValueError:
        return -1

