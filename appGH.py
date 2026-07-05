import os
import moduloGH


def main():
    productos = {
        "P101": ["Cuaderno", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }

    inventario = {"P101": [30, 15], "P102": [120, 50], "P103": [0, 10], "P104": [8, 25]}

    while True:

        os.system("cls")
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

        if opcion == 1:
            os.system("cls")
            categoria = str(input("Ingrese la categoria a buscar: "))
            moduloGH.stock_categoria(categoria, productos, inventario)
            os.system("pause")

        ################################################

        elif opcion == 2:
            os.system("cls")
            try:
                precio_min = int(input("Ingrese el precio minimo: "))
                precio_max = int(input("Ingrese el precio maximo: "))
                if precio_min >= 0 and precio_max > precio_min:
                    moduloGH.buscar_precio(
                        precio_min, precio_max, productos, inventario
                    )
                else:
                    print("Error, precios no validos")
            except ValueError:
                print("Error, debe ingresar numeros enteros")
            os.system("pause")

        ################################################

        elif opcion == 3:
            os.system("cls")
            continuar = "s"
            while continuar.lower() == "s":
                cod = input("Ingrese el código del producto a actualizar: ")
                if moduloGH.buscar_codigo(cod, productos):
                    try:
                        nuevo_p = int(input("Ingrese el nuevo precio: "))
                        if moduloGH.validar_precio(nuevo_p):
                            moduloGH.actualizar_precio(cod, nuevo_p, productos)
                            print("¡Precio actualizado con éxito!")
                        else:
                            print("Error, el precio debe ser mayor que cero.")
                    except ValueError:
                        print("Error, debe ingresar un número entero.")
                else:
                    print("Código inexistente.")

                print("-------------------------------------")
                continuar = input("¿Desea actualizar otro precio? (s/n): ")

        ##################################################

        elif opcion == 4:
            os.system("cls")
            print("--- Agregar nuevo producto ---")

            while True:
                cod = str(input("Ingrese el codigo del producto: "))
                if moduloGH.validar_codigo(cod, productos):
                    break
                print("Error, código vacío o ya existente")

            while True:
                nom = str(input("Ingrese el nombre del producto: "))
                if moduloGH.validar_nombre(nom):
                    break
                print("Error, el nombre no puede estar vacío")

            while True:
                cat = str(input("Ingrese la categoria: "))
                if moduloGH.validar_categoria(cat):
                    break
                print("Error, la categoría no puede estar vacía")

            while True:
                try:
                    precio = int(input("Ingrese el precio del producto: "))
                    if moduloGH.validar_precio(precio):
                        break
                    print("Error, el precio debe ser un entero mayor que cero")
                except ValueError:
                    print("Error, precio no valido")

            while True:
                disp_in = str(input("¿Este producto esta disponible?: S/N "))
                if moduloGH.validar_disponible(disp_in):
                    disponible = True if disp_in.strip().lower() == "s" else False
                    break
                print("Error, debe responder con S o N")

            while True:
                try:
                    stock = int(input("Ingrese el stock del producto: "))
                    if moduloGH.validar_stock(stock):
                        break
                    print("Error, el stock debe ser un entero mayor o igual a cero")
                except ValueError:
                    print("Error, stock no valido")

            while True:
                try:
                    vendidos = int(
                        input("Ingrese la cantidad de ventas del producto: ")
                    )
                    if moduloGH.validar_vendidos(vendidos):
                        break
                    print("Error, las ventas deben ser un entero mayor o igual a cero")
                except ValueError:
                    print("Error, cantidad no valida")

            exito = moduloGH.agregar_producto(
                cod,
                nom,
                cat,
                precio,
                disponible,
                stock,
                vendidos,
                productos,
                inventario,
            )
            if exito:
                print("¡Producto agregado exitosamente!")
            else:
                print("Error al guardar el producto.")

            input("Presione Enter para volver al menú...")

        ########################################

        elif opcion == 5:
            os.system("cls")
            cod = str(input("Ingrese el código del producto a eliminar: "))
            if moduloGH.eliminar_producto(cod, productos, inventario):
                print("Producto eliminado correctamente.")
            else:
                print("Código inexistente.")
            os.system("pause")

        #########################################

        elif opcion == 6:
            os.system("cls")
            moduloGH.mostrar_productos(productos, inventario)
            os.system("pause")

        #########################################

        elif opcion == 7:
            os.system("cls")
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Error, opcion no valida")


if __name__ == "__main__":
    main()
