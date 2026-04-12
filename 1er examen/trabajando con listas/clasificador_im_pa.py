def contadores(V):
    c_impares = 0
    c_pares = 0
    for numero in V:
        if numero % 2 == 0:
            c_pares += 1
        elif numero % 2 == 1:
            c_impares += 1
    return c_impares, c_pares

numeros = [2, 5, 6, 11, 8, 12]
resultados=contadores(numeros)
print(f"La cantidad de impares es: {resultados[0]}")
print(f"La cantidad de pares es: {resultados[1]}")

