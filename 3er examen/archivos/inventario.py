def crea_archivo():
    with(open("productos.txt", "w")) as inventario:
        contenido = inventario.write("")

def agregar_producto():
    with(open("productos.txt", "a")) as inventario:
        nombre = input("Ingrese el nombre del producto: ")  
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        inventario.write(f"{nombre}, {precio}, {cantidad} \n")

def calcular_valor_inventario():
    with(open("productos.txt", "r")) as inventario:
        total = 0
        for linea in inventario:
            V = linea.split(",")
            total += int(V[1]) * int(V[2])
    print(f"El valor total del inventario es: {total}")


def mostrar_inventario():
    with(open("productos.txt", "r")) as inventario:
        contenido = inventario.read()
        print(contenido)

crea_archivo()
agregar_producto()
agregar_producto()
mostrar_inventario()
calcular_valor_inventario()