def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)

n = int(input("Ingrese un numero: "))
suma = 0
while n > 0:
    numero = n % 10
    if numero % 2 == 0:
        factorial(numero)
    elif numero % 2 == 1:
        suma += numero
    n //= 10

print(f"La suma de digitos impares es: {suma}")