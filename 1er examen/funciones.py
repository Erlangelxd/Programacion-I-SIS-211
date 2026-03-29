# Procedimiento
def saludar(nombre):
    print(f"Hola {nombre}")
#saludar("Erlan")
def verificar_edad(edad):
    if edad >= 0 and edad <= 18:
        return False
    elif edad >= 18 and edad <= 25:
        return True
    elif edad >= 25 and edad <= 60:
        return True
    else:
        return True

def permiso(edad):
    if verificar_edad(edad):
        print("Ingreso permitido")
    else:
        print("Ingreso no permitido")

edad = int(input("Ingrese su edad: "))
permiso(edad)
