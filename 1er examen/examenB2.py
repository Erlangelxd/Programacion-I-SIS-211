def primer_digito(n):
    pos = 0
    while n > 0:
        digito = n % 10
        n //= 10
        pos = digito
    return pos

n = int(input("Ingrese un numero: "))
a = primer_digito(n)
resultado = 0

while n > 0:
    digito = n % 10
    resultado += digito**a
    n //= 10

print(f"Primer dígito: {a}")
print(f"Resultado: {resultado}")