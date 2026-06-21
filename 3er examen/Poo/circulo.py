import math

class Circulo:
    def __init__(self):
        self.posx = None
        self.posy = None
        self.radio = None
    def leer(self):
        self.posx = int(input("Pos x: "))
        self.posy = int(input("Pos y: "))
        self.radio = float(input("Radio: "))
    def mostrar(self):
        print(f"Posx: {self.posx}, Posy: {self.posy}, Radio: {self.radio}")
    def area(self):
        area = math.pi * self.radio**2
        print(f"Area: {area}")
    def circunferencia(self):
        circunferencia = 2*math.pi*self.radio
        print(f"Circunferencia: {circunferencia}")
    def diametro(self):
        diametro = 2*self.radio
        print(f"Diametro: {diametro}")

figura = Circulo()
figura.leer()
figura.mostrar()
figura.area()
figura.circunferencia()
figura.diametro()