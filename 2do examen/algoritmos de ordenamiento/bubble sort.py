def agrega(V, n):
    for i in range(0, n):
        valor = int(input("Ingrese el valor a agregar: "))
        V[i] = valor

def mostrar(V, n):
    for i in range(0, n):
        print(V[i], end=", ")

def ordenamiento_burbuja(V, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if V[j] < V[i]:
                V[i], V[j] = V[j], V[i]
            """
                aux = V[i]
                V[i] = V[j]
                V[j] = aux
            """

n = int(input("Longitud: "))
V = [0]*n
agrega(V, n)
print(V)
ordenamiento_burbuja(V, n)
print(V)