def calcular_pascua(anio):
    A = anio % 19
    B = anio % 4
    C = anio % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7
    dia = 22 + D + E
    if dia <= 31:
        mes = "marzo"
        dia_pascua = dia
    else:
        mes = "abril"
        dia_pascua = dia - 31
    print(f"El Domingo de Pascua para el año {anio} es el {dia_pascua} de {mes}")

anio = int(input("Ingrese el año para calcular el Domingo de Pascua: "))
calcular_pascua(anio)
