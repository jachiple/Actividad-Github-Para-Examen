# MODULO !!!
# codigo es la llave y datos son los valores asociados a la llave


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
        return val >= 0
    except ValueError:
        return False


def validar_stock(stock):
    try:
        val = int(stock)
        return val >= 0
    except ValueError:
        return False


def validar_disponible(opcion):
    opdis = opcion.strip().lower()
    if opdis == "s" or opdis == "n":
        return True
    else:
        return False


def validar_vendidos(vendidos):
    try:
        val = int(vendidos)
        return val > 0
    except ValueError:
        return False


###################################################################################


def leer_opcion():
    try:
        opcionmod = int(input("Seleccione una opción: "))
        if 1 <= opcionmod <= 7:
            return opcionmod
        else:
            return -1
    except ValueError:
        return -1


def stock_categoria(categoria, productos, inventario):
    buscar_cat = categoria.strip().lower()
    total_stock = 0
    encontrado = False

    for codigo, datos in productos.items():
        if datos[1].lower() == buscar_cat:
            encontrado = True
            total_stock += inventario[codigo][0]
    if encontrado:
        print(f"El stock para la categoria {buscar_cat} es {total_stock}")
    else:
        print(f"No se encontro stock en la categoria {buscar_cat}")


def buscar_precio(precio_min, precio_max, productos, inventario):
    coincidencias = []
    for codigo, datos in productos.items():
        nombre = datos[0]
        precio = datos[2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:
            coincidencias.append((nombre, codigo))

    if coincidencias:
        coincidencias.sort()
        print("---Productos Encontrados (Disponibles)---")
        for nombre, codigo in coincidencias:
            print(f"{nombre}---{codigo}")

    else:
        print("No se encontraron productos")


def buscar_codigo(codigo, productos):
    codigoval = codigo.strip().upper()
    if codigoval in productos:
        return True
    else:
        return False


def actualizar_precio(codigo, nuevo_precio, productos):
    cod = codigo.strip().upper()
    if cod in productos:
        productos[cod][2] = nuevo_precio
        return True
    return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    cod = codigo.strip().upper()
    if cod in productos:
        return False

    productos[cod] = [nombre.strip(), categoria.strip(), precio, disponible]
    inventario[cod] = [stock, vendidos]
    return True


def eliminar_producto(codigo, productos, inventario):
    cod = codigo.strip().upper()
    if cod in productos:
        del productos[cod]
        del inventario[cod]
        return True
    return False


def mostrar_productos(productos, inventario):
    if not productos:
        print("No hay productos registrados en el sistema")
        return False
    for codigo in productos:
        print(f"CODIGO: {codigo}")
        print("--------------------------")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoría: {productos[codigo][1]}")
        print(f"Precio: ${productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")
        print("--------------------------")
    return True
