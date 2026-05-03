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


n = int(input("Longitud"))
V = [0]*n
llena(V, n)
print(V)
seleccion(V, n)
print(V)




