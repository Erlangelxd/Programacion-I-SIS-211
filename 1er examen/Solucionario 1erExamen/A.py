repe = int(input("N: "))
for i in range(repe):
    suma = 0
    entrada = int(input("Ingrese a: "))
    while entrada > 0:
        digito = entrada % 10
        suma += digito
        entrada //= 10
    print(f"Salida: {suma}")