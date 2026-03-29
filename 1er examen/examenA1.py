def factorial(n):
    resultado = 1
    for numero in range(1, n+1):
        resultado = resultado * numero
    return resultado

def suma(x, y):
    return x + y

def divide(x, y):
    return x / y

def main():
    n = int(input("Ingrese N: "))
    r = int(input("Ingrese R: "))
    res = divide(factorial(suma(n, r)) , suma(factorial(n), factorial(r)))
    print(res)

main()