numeros = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 7, 9, 10]
sin_repetidos = []
for i in numeros:
    if i not in sin_repetidos:
        sin_repetidos.append(i)
print(sin_repetidos)