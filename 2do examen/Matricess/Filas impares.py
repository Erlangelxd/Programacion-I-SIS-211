import random
def llena(M, n, m):
    for i in range(n):
        for j in range(m):
            M[i][j] = random.randint(1, 9)

def mostrar(M, n, m):
    for i in range(n):
        for j in range(m):
            print(M[i][j], end=" ")
        print()

def ordenaImpares(M, n, m):
    for fila in range(n):
        if fila % 2 != 0:
            for reco in range(m):
                for columna in range(m-1):
                    if M[fila][columna] > M[fila][columna+1]:
                        aux = M[fila][columna]
                        M[fila][columna] = M[fila][columna+1]
                        M[fila][columna+1] = aux


m = int(input("Dimencion: "))
n = int(input("Dimencion: "))
M = [[0]*m for i in range(n)]
llena(M, n, m)
mostrar(M, n, m)
ordenaImpares(M, n, m)
print("\n")
mostrar(M, n, m)