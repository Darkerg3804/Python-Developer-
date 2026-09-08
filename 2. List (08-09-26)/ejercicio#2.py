# Ejercicio 2
# Crea una función que reciba una lista de números y devuelva
# cuántos elementos son positivos.

def contarpositivos (lista):
    contar = 0 
    for i in lista:
       if i > 0:
           contar += 1

    return contar

lista =[1,2,3,4,-5]

print(contarpositivos(lista))