def crear_archivo():
    with (open("ejemplo.txt", "w")) as archivo:
        archivo.write("")

def añade_RU():
    with(open("ejemplo.txt", "a")) as archivo:
        ru = input("Introduce tu RU: ")
        archivo.write(ru + "\n")

def leer_RUs():
    with(open("ejemplo.txt", "r")) as archivo:
        contenido = archivo.read()
        print(contenido)

crear_archivo()
estudiantes = int(input("¿Cuántos estudiantes deseas agregar? "))
for i in range(estudiantes):
    añade_RU()
leer_RUs()