def verifica_progresion1(V):
    comun = V[1] - V[0] / (2 - 1)
    return int(comun)

def verifica_progresion2(V):
    comun = V[len(V)-1] - V[len(V)-2] / (2 - 1)
    return int(comun)

def verifica_progresion3(V):
    mitad = len(V)//2
    comun = V[mitad] - V[mitad-1] / (2 - 1)
    return int(comun)

def fix_prank_number(arr):
    Ideal = []
    if verifica_progresion1(arr) == verifica_progresion2(arr) == verifica_progresion3(arr):
        for i in range(verifica_progresion1(arr), (len(arr) * verifica_progresion1(arr)) + 1,verifica_progresion1(arr)):
            Ideal.append(i)
        return Ideal
    elif verifica_progresion2(arr) != verifica_progresion3(arr) or verifica_progresion3(arr) != verifica_progresion1(arr):
        pr = max(verifica_progresion1(arr), verifica_progresion2(arr), verifica_progresion3(arr))
        for i in range(pr, (len(arr) * pr) + 1, pr):
            Ideal.append(i)
        return Ideal

V = [2, 31, 6, 8, 10, 12, 14]
print(fix_prank_number(V))


"""
    elif verifica_progresion2(arr) != verifica_progresion3(arr) or verifica_progresion3(arr) != verifica_progresion1(arr):
        pr = max(verifica_progresion1(arr), verifica_progresion2(arr), verifica_progresion3(arr))
        for i in range(pr, (len(arr) * pr) + 1,pr):
            Ideal.append(i)
        return Ideal
"""
