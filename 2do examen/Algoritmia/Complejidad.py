# O(1)   Constante

V=[3, 2, 1, 2, 43]

def obtenerSegundoElemento(V):
    return V[1]

# O(n)   Lineal

def SumaLista(V):
    suma = 0
    for i in range(len(V)):
        suma += V[i]
    return suma

# O(n^2)   Cuadratica

def ordenamiento_burbuja(V, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if V[j] < V[i]:
                V[i], V[j] = V[j], V[i]

# O(log n)   Logaritmica

def busquedaBinaria(V, n, objetivo):
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