def crea():
    with(open("amigos.txt", "w")) as archivo:
        archivo.write("")

def agregar_amigo():
    with(open("amigos.txt", "a")) as archivo:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        departamento = input("Departamento: ") 
        archivo.write(f"{nombre}, {edad}, {departamento} \n")

def mostrar_amigos():
    with(open("amigos.txt", "r")) as archivo:
        for linea in archivo:
            print(linea)

def buscar_lugar_nacimiento():
    with(open("amigos.txt", "r")) as archivo:
        x = input("Ingrese el departamento a buscar: ")
        for linea in archivo:
            V = linea.split(",") 
            if x.upper() == V[2].strip().upper():
                print(f"Nombre: {V[0]}, Edad: {V[1]}, Departamento: {V[2]}")
crea()
agregar_amigo()
agregar_amigo()
mostrar_amigos()
buscar_lugar_nacimiento()