import random
def llenar(M,n,m):
    for i in range(n):
        for j in range(m):
            M[i][j]=random.randint(1,10)

def mostrar(M,n,m):
    for i in range (n):
        for j in range(m):
            print(M[i][j], end=" ")
        print()

def solucion(M,n,m):
    for i in range (n):
        if i % 2 == 0:
            for recorrido in range(m):    
                for j in range(m-1):
                    if M[i][j]>M[i][j+1]:
                        M[i][j], M[i][j+1] = M[i][j+1], M[i][j]

n=int(input("ingrese n: "))
m=int(input("ingrese m: "))
M= [[0]*m for i in range(n)]
llenar(M,n,m)
mostrar(M,n,m)
print("Matriz ordenada: ")
solucion(M,n,m)
mostrar(M,n,m)