"""
ENTRADAS
notas_auxiliar=[7, 5, 10, 30] 0 <= nota <= 10
nota_ingeniero=[70, 40, 90, 3] 0 <= nota <= 90
SALIDA
Estado=['Aprovado', 'Reprobado', 'Aprovado', 'Reprobado']
"""

notas_auxiliar=[7, 5, 10, 30]
nota_ingeniero=[70, 40, 90, 3]
estado = [0, 0, 0, 0]
for i in range(0, len(notas_auxiliar)):
    total = notas_auxiliar[i] + nota_ingeniero[i]
    if total >= 51:
        estado[i] = "Aprovado"
    else:
        estado[i] = "Reprobado"

print(estado)