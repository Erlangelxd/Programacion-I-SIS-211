def Llena(V, n):
    for i in range(n):
        valor = int(input("Ingrese un valor: "))
        V[i] = valor

def busquedaLineal(V,n, target):
    for i in range(n):
        if target == V[i]:
            print("Encontrado")

n = int(input("Longitud: "))
V = [0]*n
Llena(V, n)
target = int(input("Que numero quieres buscar?: "))
busquedaLineal(V, n, target)

