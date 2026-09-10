# Ejercicio 1
# Crea una función que reciba una lista de números y devuelva
# la suma de todos sus elementos.

def sumaLista (lt):
    suma = 0 
    for i in lt:
        suma += i

    return suma

lista =[1,2,3,4,-5]

print(sumaLista(lista))