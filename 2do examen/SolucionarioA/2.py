import random
def llenar(V, n):
    for i in range(n):
        valor = random.randint(1, 9)
        V[i] = valor

def contruyeMatriz(M, V1, V2, n):
    for i in range(n):
        M[i][0] = V1[i]
        M[i][1] = V2[i]

def mostrar(M, n):
    for i in range(n):
        for j in range(2):
            print(M[i][j], end=" ")
        print()

n = int(input("Dimencion de la matriz: "))
M = [[0]*2 for i in range(n)]
V1 = [0]*n
V2 = [0]*n
llenar(V1, n)
llenar(V2, n)
print(V1)
print(V2)
contruyeMatriz(M, V1, V2, n)
mostrar(M, n)