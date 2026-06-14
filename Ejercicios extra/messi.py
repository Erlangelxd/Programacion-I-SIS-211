def matriz_superior(n, m):
    cont = 1
    inicio = 1
    matriz =  [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m - inicio):
            matriz[i][j] = cont
            cont += 1
        inicio += 1
    return matriz

def matriz_inferior(n, m, matriz):
    cont = 1
    inicio = 0
    for i in range(1, n):
        for j in range(m-1-inicio, m):
            matriz[i][j] = cont
            cont += 1
        inicio += 1
    return matriz

matriz1 = matriz_superior(5, 4)
matriz2 = matriz_inferior(5, 4, matriz=matriz1)

for i in matriz2:
    print(i)
        