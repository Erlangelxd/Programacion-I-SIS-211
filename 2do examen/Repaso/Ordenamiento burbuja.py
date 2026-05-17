import random
def llenar(V, n):
    for i in range(n):
        valor = random.randint(10, 999)
        V[i] = valor
def ordenamiendoBurbuja(V, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if V[j] < V[i]:
                #V[i], V[j] = V[j], V[i]
                aux = V[i]
                V[i] = V[j]
                V[j] = aux

n = int(input("Longitud: "))
V = [0]*n
llenar(V, n)
print(V)
ordenamiendoBurbuja(V, n)
print(V)