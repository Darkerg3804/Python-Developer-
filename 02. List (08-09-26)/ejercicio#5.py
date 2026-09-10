# Ejercicio 5
# Crea una función que reciba una lista de números y devuelva
# dos listas: una con los números pares y otra con los números impares.

def paridad (lista):
    pares =[]
    impares = []
    for i in lista:
        if (i%2) == 0:
            pares.append(i)
        else:
            impares.append(i)

    return [pares,impares]

lista10 = [1,2,3,4,5,6,7,8,9,10]
print(paridad(lista10))
        