def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

def primo(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

n = int(input("N: "))
while n > 0:
    digito = n % 10
    if primo(digito):
        print(factorial(digito))
    n = n // 10