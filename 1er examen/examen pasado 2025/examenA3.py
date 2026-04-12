def primo(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

def llenarVector(V):
    for i in range(0, dimencion):
        valor = int(input("Valor: "))
        V[i] = valor

def resolucion(V, R):
    for i in range(0, dimencion):
        if primo(V[i]):
            R[i] = 2
        else:
            R[i] = V[i]

def mostrar(V):
    for i in range(0, dimencion):
        print(V[i], end=" ")


dimencion = int(input("Dimencion: "))
V = [0]*dimencion
R = [0]*dimencion
llenarVector(V)
resolucion(V, R)
print(V)
print(R)