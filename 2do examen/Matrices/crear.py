import random
def llena(M, n):
    for i in range(n):
        for j in range(n):
            M[i][j] = 0

def mostrar(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=" ")
        print()

def columna1(M, n):
    for i in range(n):
        for j in range(n):
            if j == 0:
                M[i][j] = 1

def columna2(M, n):
    for i in range(n):
        for j in range(n):
            if j == n-1:
                M[i][j] = 1

def diagonalPrincipalInversa(M, n):
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                M[i][j] = 1

n = int(input("Dimencion: "))
M = [[0]*n for i in range(n)]
llena(M, n)
columna1(M, n)
columna2(M, n)
diagonalPrincipal(M, n)
mostrar(M, n)