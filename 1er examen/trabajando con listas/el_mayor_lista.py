def mayor(V):
    may = V[0]
    for i in range(1, 8):
        if V[i] > may:
            may = V[i]
    return may

calificaciones = [1, 90, 100, 80, 30, 55, 60, 9999]
print(f"El valor mas grande de la lista es: {mayor(calificaciones)}")