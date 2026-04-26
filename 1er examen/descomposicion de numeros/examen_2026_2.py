n = int(input("N: "))

for i in range(1, n+1):
    numero = int(input("Digite a: "))
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    print(f"Salida: {suma}")