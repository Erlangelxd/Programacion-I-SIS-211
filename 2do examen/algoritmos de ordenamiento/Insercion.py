def Llena(V, n):
    for i in range(n):
        valor = int(input("Ingrese un valor: "))
        V[i] = valor

def Insercion(V, n):
    for j in range(1, n):
        actual = V[j]
        i = j - 1
        while i >= 0 and V[i] > actual:
            V[i+1] = V[i]
            i -= 1
        V[i+1] = actual

n = int(input("longitud: "))
V = [0]*n
Llena(V, n)
print(V)
Insercion(V, n)
print(V)