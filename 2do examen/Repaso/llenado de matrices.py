import random
def llena(M, n):
    for i in range(n):
        for j in range(n):
            M[i][j] = random.randint(1, 9)
def mostrar(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=" ")
        print()

n = int(input("Dimencion de la matriz: "))
M = [[0]*n for i in range(n)]
llena(M, n)
mostrar(M, n)
