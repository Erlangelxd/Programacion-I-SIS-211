V=[4, 12, 19, 81, 9, 14, 6]

def ordenamiento_de_multiplos_de_3(V):
    multiplos = []
    for num in V:
        if num % 3 == 0:
            multiplos.append(num)
    multiplos.sort()
    for i in range(len(V)):
        if V[i] % 3 == 0:
            V[i] = multiplos.pop(0)

print("Vector original:", V)
ordenamiento_de_multiplos_de_3(V)
print("Vector ordenado:", V)