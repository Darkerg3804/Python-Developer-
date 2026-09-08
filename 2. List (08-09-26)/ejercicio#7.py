# Ejercicio 7
# Crea una función que reciba una lista y un número n.
# La función debe desplazar los elementos de la lista n posiciones
# hacia la derecha.
#
# Ejemplo:
# [1, 2, 3, 4, 5], 2
# Resultado: [4, 5, 1, 2, 3]

def rotar_n_lista(lista,n):
    nuevalista = []
    tira = len(lista)

    if tira < n:
        n = n % tira
    
    for i in range(tira):
        nuevalista.append(lista[-n+i])

    return nuevalista

a = [0,1,2,3,4,5,6]

print(rotar_n_lista(a,9))