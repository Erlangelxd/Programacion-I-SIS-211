import random
def llenar(V, n):
    for i in range(n):
        valor = random.randint(10, 999)
        V[i] = valor

n = int(input("Longitud: "))
V = [0]*n
llenar(V, n)
print(V)