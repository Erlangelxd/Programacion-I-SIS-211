import time

def busquedaLineal(V,n, target):  # 0.002803802490234375s
    for i in range(n):
        if target == V[i]:
            print("Encontrado")

def busquedaBinaria(V, n, objetivo): # 5.841255187988281e-05
    izquierda = 0
    derecha = n - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        if objetivo == V[mitad]:
            return mitad
        elif V[mitad] < objetivo:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return -1

V = [i for i in range(50000)]

inicio = time.time()
#busquedaLineal(V, 50000, 30000)
busquedaBinaria(V, 50000, 30000)
fin = time.time()
tiempo = fin - inicio
print("Tiempo de busqueda binaria: ", tiempo)
