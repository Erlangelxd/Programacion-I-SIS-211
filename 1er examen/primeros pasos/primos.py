def verificaPrimos(numero):
    c = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

n = int(input("N: "))
print(verificaPrimos(n))