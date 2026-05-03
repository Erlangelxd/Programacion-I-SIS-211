import string
def get_word_score(word):
    dic = {clave: valor + 1 for valor, clave in enumerate(string.ascii_lowercase)}
    suma = 0
    for letra in word.lower():
        suma += dic[letra]
    return suma

print(get_word_score("freeCodeCamp"))