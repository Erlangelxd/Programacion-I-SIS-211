def crear(nombre_archivo):
    with(open(nombre_archivo, "w")) as archivo:
        archivo.write("")

def agregar_linea(nombre_archivo):
    with(open(nombre_archivo, "a")) as archivo:
        apellido = input("Ingrese el apellido de la persona: ")
        nombre = input("Ingrese el nombre de la persona: ")
        sexo = input("Ingrese el sexo de la persona (M/F): ")
        archivo.write(f"{apellido}, {nombre}, {sexo} \n")

def filtrar():
    with(open("personas.txt", "r")) as archivo:
        for linea in archivo:
            V = linea.split(",")
            if V[2].strip().upper() == "M":
                with(open("varones.txt", "a")) as varones:
                    varones.write(linea + "\n")
            elif V[2].strip().upper() == "F":
                with(open("mujeres.txt", "a")) as mujeres:
                    mujeres.write(linea + "\n")

crear("personas.txt")
crear("varones.txt")
crear("mujeres.txt")
agregar_linea("personas.txt")
agregar_linea("personas.txt")
agregar_linea("personas.txt")
agregar_linea("personas.txt")
filtrar()