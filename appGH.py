import os
import moduloGH


def main():
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }

    inventario = {"P101": [30, 15], "P102": [120, 50], "P103": [0, 10], "P104": [8, 25]}


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("======================")

    opcion = moduloGH.leer_opcion()
