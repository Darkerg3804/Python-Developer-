# Ejercicio 6
# Crea una función que reciba una lista de números y devuelva
# el segundo número más grande.
# No utilices sort() ni sorted().
# Si existen valores repetidos, considera únicamente valores diferentes.

def segundomaximo (lista):
    maxim = lista[0]
    segundo = lista[0]
    for i in lista:
        if i > maxim:
            segundo = maxim
            maxim = i
        elif i > segundo:
            segundo = i

    return segundo

lista =[1,2,3,4,-5,9]

print(segundomaximo(lista))
    