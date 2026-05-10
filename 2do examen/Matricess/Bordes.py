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

def contador(M, n, objetivo):
    c = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if M[i][j] == objetivo:
                    c += 1
    return c
n = int(input("Dimencion: "))
M = [[0]*n for i in range(n)]
llena(M, n)
mostrar(M, n)
print(f"c = {contador(M, n, 5)}")
mostrar(M, n)
