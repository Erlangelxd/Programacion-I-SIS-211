edades = [20, 18, 22, 17, 12, 21] #trabajando con listas
tuplas = (20, 18, 21, 17) #tuplas
estut = {
    "Nombre":"Erlan",
    "Edad":20
} #diccionarios

print("Primer metodo")
for edad in edades:
    print(edad)
print("Segundo metodo")
for i in range(len(edades)):
    print(edades[i])

