# Ejercicio 3
# Crea una función que reciba una lista de números y devuelva
# el número mayor.
# No utilices la función max(). Debes recorrer la lista.

def maximo (lista):
    maxim = lista[0]
    for i in lista:
        if i > maxim:
            maxim = i

    return maxim

lista =[1,2,3,4,-5]

print(maximo(lista))