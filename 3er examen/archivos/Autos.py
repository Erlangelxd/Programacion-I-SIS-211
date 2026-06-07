def crear_autos():
    with(open("Autos.txt","w"))as texto:
        contenido = texto.write("")
def marca_auto():
    with(open("Autos.txt","a"))as texto:
        marca_auto = input("Ingrese la marca del auto:  ")
        texto.write(marca_auto + "\n")
def matricula_auto():
    with(open("Autos.txt","a"))as texto:
        matricula_auto = input("Ingrese la matrícula del auto:  ")
        texto.write(matricula_auto + "\n")
def mostrar_autos():
    with(open("Autos.txt","r"))as texto:
        contenido = texto.read()
        print(contenido)

crear_autos()
marca_auto()
matricula_auto()
mostrar_autos()

#Max Zárate Fabian




    
    