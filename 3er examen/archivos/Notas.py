def crear_archivo():
    with(open("Rodrigo.txt", "w")) as texto:
        contenido = texto.write("")

def agregar_nota():
    with(open("Rodrigo.txt", "a")) as texto:
        nota=input("Ingese la materia y nota: ")
        texto.write(nota + "\n")

def leer_nota():
    with(open("Rodrigo.txt", "r")) as texto:
        contenido= texto.read
        print(contenido)

crear_archivo()
agregar_nota()
agregar_nota()
leer_nota()


