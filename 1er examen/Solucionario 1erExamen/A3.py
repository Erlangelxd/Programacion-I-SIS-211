V=[15, 6, 2, 15, 15]
n = int(input("Digite un numero: "))
contador = 0
for i in V:
    if n == i:
        contador += 1
print(f"El numero {n} se repitió {contador} veces")