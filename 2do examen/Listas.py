def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def multiplo3(V, n):
    for i in range(0, n):
        if V[i] % 3 == 0:
            print(factorial(V[i]), end= ", ")
        else:
            print(0, end= ", ")

def agrega(V, n):
    for i in range(0, n):
        valor = int(input("Valor: "))
        V[i] = valor
def mostrar(V, n):
    for i in range(0, n):
        print(V[i], end = ", ")

n = int(input("Ingrese el tamaño del vector: "))
V = [0]*n
agrega(V)
mostrar(V)
print("\n")
multiplo3(V)