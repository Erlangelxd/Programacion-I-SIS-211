"""
ENTRADAS
longitud=5   --> 2/1!+4/2!-6/3!+8/4!-10/5!....
SALIDA
resultado = 2/1!+4/2!-6/3!+8/4!-10/5!
"""
def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado


n = int(input("Ingrese un numero: "))

resultado = 0
signo = 1
for i in range(1,n+1):
    if signo == 1:
        resultado = resultado + i*2 / factorial(i)
        signo = 0
    elif signo == 0:
        resultado = resultado - i * 2 / factorial(i)
        signo = 1
print(resultado)



"""
a, b, c
SALIDA
resultado = (a+b)! - (c+a)! / (a!+b!+c!)
"""
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese otro numero: "))
resultado = factorial(a+b) - factorial(c+a) / (factorial(a) + factorial(b) + factorial(c))
print(resultado)