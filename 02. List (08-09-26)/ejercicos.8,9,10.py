# Ejercicio 8
# Crea una función que reciba una lista y devuelva un diccionario
# indicando cuántas veces aparece cada elemento.
#
# No utilices collections.Counter.

def cantidad_elementos_lista(lista):
    dic = {}

    for i in lista:
        if not (i in dic):
            dic[i] = 1
        else:
            dic[i] += 1

    return dic


# Ejercicio 9
# Crea una función que reciba una lista de números y devuelva
# la longitud de la mayor secuencia de elementos consecutivos iguales.
#
# Ejemplo:
# [1, 1, 2, 2, 2, 3, 3, 1]
# Resultado: 3
def contarsecuencia (lista):
    n = 0
    m = 0
    elemento = None


    for i in lista:

        if i == elemento:
            n += 1
        else:
            elemento = i
            n = 1

        if m < n:
            m = n

    return m     
            

# Ejercicio 10
# Crea una función que reciba una lista y agrupe los elementos
# consecutivos iguales.
#
# La función debe devolver una lista de tuplas donde cada tupla
# contenga el elemento y la cantidad de veces que aparece
# consecutivamente.
#
# Ejemplo:
# ["a", "a", "a", "b", "b", "c", "a", "a"]
#
# Resultado:
# [("a", 3), ("b", 2), ("c", 1), ("a", 2)]

def agrupacionlista (lista):
    n = 0
    elemento = None
    nuevalista = []


    if len(lista) != 0:
        elemento = lista[0]

    for i in lista:
        if i == elemento:
            n += 1
        else:
            nuevalista.append((elemento,n))
            elemento = i
            n = 1

    if len(lista) != 0:
        nuevalista.append((elemento,n))        

    return nuevalista
        

        
        
