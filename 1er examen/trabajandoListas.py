V = [1, 2, 3, 4, 5, 6]

for i in range(len(V)):
    V[i] = V[i] * 2

print(V)

n = int(input("Ingrese la longitud: "))
V = [0]*n
for i in range(n):
    V[i] = int(input("Ingrese el valor: "))

print(V)
