import random
def llenadoTriangularInferior(M, n):
    for i in range(n):
        for j in range(n):
           if i > j:
               M[i][j] = 99

def llenado(M, n):
    for i in range(n):
        c = 1
        for j in range(n):
            if i == j:
                M[i][j] = c
            c += 1

def mostrar(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="         ")
        print()

def llenaMatriz(M, n):
    c = 1
    for g in range(n):
        M[g][g] = c
        c += 1
    for j in range(1, n):
        for i in range(j):
            M[i][j] = c
            c += 1
n = int(input("Dimencion de la matriz: "))
M = [[0]*n for i in range(n)]
llenaMatriz(M, n)
llenadoTriangularInferior(M, n)
mostrar(M, n)
