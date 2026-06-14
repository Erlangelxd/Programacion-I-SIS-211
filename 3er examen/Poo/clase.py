def suma(x, y):
    return x + y

class Operaciones:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def suma(self):
        return self.x + self.y
    def resta(self):
        return self.x - self.y
    def multiplicacion(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y

print(suma(2, 3))

resultado = Operaciones(2, 3)
print(resultado.suma())
print(resultado.multiplicacion())
