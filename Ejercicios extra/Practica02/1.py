def agrega(V, n):
    for i in range(0, n):
        valor = int(input("Ingrese el valor a agregar: "))
        V[i] = valor

def mostrar(V, n):
    for i in range(0, n):
        print(V[i], end=", ")

def ordenamiento_burbuja(V, n):
    for i in range(1, n, 2):
        for j in range(1, n-2, 2):
            if V[j] < V[i]:
                V[i], V[j] = V[j], V[i]

n = int(input("Longitud: "))
V = [0]*n
agrega(V, n)
print(V)
ordenamiento_burbuja(V, n)
print(V)