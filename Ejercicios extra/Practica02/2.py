def Llena(V, n):
    for i in range(n):
        valor = int(input("Ingrese un valor: "))
        V[i] = valor

def insertion_sort_impares(V):
    n = len(V)
    for i in range(n):
        if V[i] % 2 == 0:
            continue
        actual = V[i]
        j = i - 1
        while j >= 0:
            if V[j] % 2 == 0:
                j -= 1
                continue
            if V[j] > actual:
                k = j + 1
                while V[k] % 2 == 0:
                    k += 1
                V[k] = V[j]
                j -= 1
            else:
                break
        k = j + 1
        while k < i and V[k] % 2 == 0:
            k += 1
        V[k] = actual


n = int(input("longitud: "))
V = [0]*n
Llena(V, n)
print(V)
insertion_sort_impares(V)
print(V)