def digitos(n):
    contador = 0
    while n > 0:
        contador += 1
        n //= 10
    return contador

def verificar(V):
    pos = 0
    val = 0
    may = digitos(V[0])
    for i in range(1,len(V)):
        if digitos(V[i]) > may:
            may = digitos(V[i])
            pos = i
            val = V[i]
    print(f"digitos: {val}")
    print(f"posicion: {pos}")

V = [21, 323, 4343, 111111, 222222222]
verificar(V)