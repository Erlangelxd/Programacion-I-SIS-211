def clasificaEstudiantes(notas):
    for posicion in range(n):
        nota = int(input("Nota: "))
        notas[posicion] = nota
        if notas[posicion] >= 51:
            estado[posicion] = "Aprobado"
        else:
            estado[posicion] = "Reprobado"

n = int(input("Longitud: "))
notas = [0]*n
estado = [0]*n
clasificaEstudiantes(notas)
print(notas)
print(estado)
