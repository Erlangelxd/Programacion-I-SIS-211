usuario = "Alexander"
contraseña = "12345"

def verificador(v_usuario, v_contraseña):
    if v_usuario == usuario and v_contraseña == contraseña:
        return True
    elif v_usuario != usuario and v_contraseña != contraseña:
        return False

def login(v_usuario, v_contraseña):
    if verificador(v_usuario, v_contraseña):
        print("Bienvenido")
    else:
        print("Error")

v_usuario = input("Ingrese su usuario: ")
v_contraseña = input("Ingrese su contraseña:")
login(v_usuario, v_contraseña)