n = int(input("N: "))
cp = 0
ci = 0
for i in range(n):
    numero = int(input("Digite un numero: "))
    if numero % 2 == 0:
        cp += 1
    elif numero % 2 == 1:
        ci += 1

if cp > ci:
    print(f"Hay mas pares: {cp}")
else:
    print(f"Hay mas impares:{ci}")
