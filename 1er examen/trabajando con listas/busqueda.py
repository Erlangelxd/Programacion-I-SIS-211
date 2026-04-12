def busqueda(V, num):
    posicion = -1
    for i in range(6):
        if V[i] == num:
            posicion = i
            break
    if posicion != -1:
        return f"El numero esta en la posicion: {posicion}"
    else:
        return f"El numero no existe en la lista"

numeros = [2, 3, 1, 9, 8, 5, 3]
n = int(input("Que numero desea buscar: "))
print(busqueda(numeros, n))