def factorial(n):
    total = 1
    for numero in range(1, n+1):
        total *= numero
    return total

n = int(input("Ingrese N: "))

while n > 0:
    digito = n % 10
    if digito % 2 == 0:
        print(factorial(digito))
    n //= 10

