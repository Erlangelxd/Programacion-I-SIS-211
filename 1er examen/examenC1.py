def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

res = 0
n = int(input("N: "))
for valor in range(1, n+1):
    res = res + (valor * 3 / factorial(valor))
print(res)
