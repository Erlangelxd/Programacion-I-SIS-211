def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def primo(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

V=[2,5,3,8,9]

"""
for numero in V:
    if primo(numero):
        print(factorial(numero))
"""

for i in range(len(V)):
    if primo(V[i]):
        print(factorial(V[i]))