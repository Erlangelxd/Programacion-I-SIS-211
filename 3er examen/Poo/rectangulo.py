class Rectangulo:
    def __init__(self):
        self.ancho = None
        self.alto = None
    def leer(self):
        self.ancho = int(input("Ingresa el ancho: "))
        self.alto = int(input("Ingresa el alto: "))
    def mostrar(self):
        print(f"Ancho: {self.ancho} Alto: {self.alto}")
    def area(self):
        area = self.ancho * self.alto
        print(f"El area del rectangulo es: {area}")
    def perimetro(self):
        perimetro = 2*(self.ancho+self.alto)
        print(f"El perimetro del rectangulo es: {perimetro}")
    
figura = Rectangulo()
figura.leer()
figura.mostrar()
figura.perimetro()
figura.area()