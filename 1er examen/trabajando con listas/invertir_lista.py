def invertido(V):
    invertido = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9, -1, -1):
        invertido[(i-9)*-1] = V[i]
    return invertido

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(invertido(numeros))
