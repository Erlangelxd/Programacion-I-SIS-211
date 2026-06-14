class Jugador:
    def __init__(self, nombre, posicion, numero, goles):
        self.nombre = nombre 
        self.posicion = posicion
        self.numero = numero
        self.goles = goles
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Posición: {self.posicion}")
        print(f"Número: {self.numero}")
        print(f"Goles: {self.goles}")
    def atacar(self):
        print(f"{self.nombre} está atacando.")
    def defender(self):
        print(f"{self.nombre} está defendiendo.")
    def meter_gol(self):
        self.goles += 1
        print(f"{self.nombre} ha metido un gol. Total de goles: {self.goles}")

jugador1 = Jugador("Messi", "Delantero", 10, 700)
jugador2 = Jugador("Ronaldo", "Delantero", 7, 700)
jugador1.mostrar_informacion()
jugador1.meter_gol()
jugador1.meter_gol()
jugador1.mostrar_informacion()


