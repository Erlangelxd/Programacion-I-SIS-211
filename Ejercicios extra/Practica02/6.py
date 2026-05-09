def ordenamiento_burbuja (V, inicio, fin):
    for i in range(inicio, fin-1):
        for j in range(i+1, fin):
            if V[j] < V[i]:
                V[i], V[j] = V[j], V[i]

V = [6, 12, 4, 5, 1, 7, 11, 9, 10]
parte = len(V) // 3
suma = []
valor = 0
for i in range(3):
    valor += V[i]
    suma.append(valor)

inicio = 0
for i in range(3):
    ordenamiento_burbuja(V, inicio, inicio + parte)
    inicio += parte
print(V)