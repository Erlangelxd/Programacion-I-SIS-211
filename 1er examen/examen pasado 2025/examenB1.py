def suma(a, b):
    return a + b

def multiplicacion(a, b, c):
    return a * b * c

#𝐴=2ℎ(𝑎+𝑏)+2𝑎𝑏
#𝑉=𝑎𝑏ℎ

lado1 = int(input("Ingrese el lado 1 del prisma: "))
lado2 = int(input("Ingrese el lado 2 del prisma: "))
altura = int(input("Ingrese el altura del prisma: "))

A = suma(multiplicacion(2, altura, suma(lado1, lado2)), multiplicacion(2, lado1, lado2))
V = multiplicacion(lado1, lado2, altura)

print(f"El area es {A}")
print(f"El volumen es {V}")


def leer(mensaje):
    n=int(input(mensaje))
    return n

def suma(a,b):
    s=a+b
    return s

def multi(a,b):
    m=a*b
    return m

a=leer("Ingrese el lado 1: ")
b=leer("Ingrese el lado 2: ")
h=leer("Ingrese el lado 3: ")
print(f"El área es: {suma(multi(2*h,suma(a,b)),multi(2*a,b))}")
print(f"El volumen es: {multi(multi(a,b),h)}")