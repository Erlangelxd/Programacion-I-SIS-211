def suma_propios(n):
    if n <= 1:
        return 0
    s = 1
    limite = int(n ** 0.5)
    for i in range(2, limite +1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

def amigos(a, b):
    if suma_propios(a) == b and suma_propios(b) == a:
        print("Los números son amigos")
    else:
        print("Los números no son amigos")

a = int(input())
b = int(input())
amigos(a, b)
