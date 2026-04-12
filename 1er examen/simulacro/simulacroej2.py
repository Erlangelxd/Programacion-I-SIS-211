"""
ENTRADAS
n = 58726
SALIDA
Primos
suma = 2!+7!+5!
"""
def primo(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False
def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado
n = int(input("N: "))
suma = 0
while n > 0:
    digito = n % 10
    if primo(digito) and digito % 2 == 0:
        suma += factorial(digito)
    n = n // 10
print(suma)

