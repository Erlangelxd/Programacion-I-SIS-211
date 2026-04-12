def suma_calificaciones(V):
    suma = 0
    for i in range(6):
        suma += V[i]
    return suma
def promedio(V):
    return suma_calificaciones(V) / 6
def clasificacion(promedio):
    if promedio>=60 and promedio <=80:
        return "Bueno"
    elif promedio>80 and promedio<=90:
        return "Execelente"
    elif promedio>90 and promedio<=100:
        return "Distinguido"

calificaciones = [90, 100, 90, 80, 98, 100]
print(f"Promedio de calificaciones: {promedio(calificaciones)} \n Clasificacion: {clasificacion(promedio(calificaciones))}")