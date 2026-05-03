def Llena(V, n):
    for i in range(n):
        valor = int(input("Ingrese un valor: "))
        V[i] = valor

def Seleccion(V, n):
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if V[minimo] > V[j]:
                minimo = j
        V[i], V[minimo] = V[minimo], V[i]

def busquedaBinaria(V, n, objetivo):
    izquierda = 0
    derecha = n - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        if objetivo == V[mitad]:
            return mitad
        elif V[mitad] < objetivo:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return -1

n = int(input("longitud: "))
V = [0]*n
Llena(V, n)
print(V)
Seleccion(V, n)
print(V)
objetivo = int(input("Ingrese un valor: "))
print(busquedaBinaria(V, n, objetivo))