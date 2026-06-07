def crea():
    with(open("pacientes.txt", "w")) as pacientes:
        contenido = pacientes.write("")

def agregar_paciente():
    with(open("pacientes.txt", "a")) as pacientes:
        ci = input("Ingrese el CI del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        pacientes.write(f"{ci}, {nombre}, {edad}, {diagnostico} \n")

def buscar_paciente():
    with(open("pacientes.txt", "r")) as pacientes:
        nombre_buscar = input("Ingrese el nombre del paciente a buscar: ")
        for linea in pacientes:
            V = linea.split(",")
            if nombre_buscar in V[1]:
                print(f"CI: {V[0]}\n Nombre: {V[1]}\n  Edad: {V[2]}\n  Diagnóstico: {V[3]}")
            

crea()
agregar_paciente()
agregar_paciente()
buscar_paciente()