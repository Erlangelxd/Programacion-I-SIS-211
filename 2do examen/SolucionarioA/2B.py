import random
def llenar(V, n):
    for i in range(n):
        valor = random.randint(1, 30)
        V[i] = valor

def descompone(num):
    digito = num % 10
    return digito

def genera(V1, V2, C, n):
    for i in range(n):
        x = descompone(V1[i])
        y = descompone(V2[i])
        C[i] = int(f"{x}{y}")

n = int(input("Longitud: "))
A = [0]*n
B = [0]*n
C = [0]*n
llenar(A, n)
llenar(B, n)
print(A)
print(B)
genera(A, B, C, n)
print(C)