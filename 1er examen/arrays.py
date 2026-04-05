def ingresar(V):
    for i in range(0, longitud):
        valor = int(input("Agrege notas: "))
        V[i] = valor

def verifica_aprovados(V):
    for i in range(0, longitud):
        if V[i] >= 5:
            print("Aprobado")
        else:
            print("Reprobado")

longitud = int(input("longitud: "))
notas=[0]*longitud
print(notas)
ingresar(notas)
print(notas)
verifica_aprovados(notas)
