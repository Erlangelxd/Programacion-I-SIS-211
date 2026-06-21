def promedioEdadVarones():
    with(open("/home/erlan/Escritorio/titanic.csv", "r")) as archivo:
        suma = 0
        personas = 0
        for linea in archivo:
            V = linea.split(",") 
            if V[1] == "masculino":
                personas += 1
                suma += int(V[2])
    promedio = suma / personas
    return promedio

def promedioEdadMujeres():
    with(open("/home/erlan/Escritorio/titanic.csv", "r")) as archivo:
        suma = 0
        personas = 0
        for linea in archivo:
            V = linea.split(",") 
            if V[1] == "femenino":
                personas += 1
                suma += int(V[2])
    promedio = suma / personas
    return promedio

def niños():
    with(open("/home/erlan/Escritorio/titanic.csv", "r")) as archivo:
        for linea in archivo:
            V = linea.split(",") 
            if 1 <= int(V[2]) and int(V[2]) <= 12:
                print(V[0])

def sobrevivientes():
    with(open("/home/erlan/Escritorio/titanic.csv", "r")) as archivo:
        mujeres = 0
        hombres = 0
        for linea in archivo:
            V = linea.split(",") 
            if V[1] == "masculino" and V[4] == "SI":
                hombres += 1
            elif V[1] == "femenino" and V[4] == "SI":
                mujeres += 1
        print(f"Varones: {hombres} \n Mujeres: {mujeres}")

print(promedioEdadVarones())
print(promedioEdadMujeres())
niños()
sobrevivientes()