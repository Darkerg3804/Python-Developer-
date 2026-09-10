# Ejercicio 4
# Crea una función que reciba una lista y devuelva una nueva lista
# sin elementos repetidos.
# Debe conservarse el orden en el que aparecen los elementos.

def sinrepetir(lista):
    nuevalista = []    

    for i in lista: 
        if i not in nuevalista:
            nuevalista.append(i)
    return nuevalista

li = [1,2,3,3,3,4,5]
print(sinrepetir(li))
        
