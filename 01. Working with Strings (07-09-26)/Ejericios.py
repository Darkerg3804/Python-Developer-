""" Ejercicio 1
Crea una función que reciba un texto y devuelva un diccionario 
con las palabras que son palíndromos y la cantidad de veces que 
aparecen en el texto, ignorando mayúsculas, minúsculas y signos
 de puntuación. """

#funcion recibe una cadena y devuelve Bool si es palindromo.
def es_palindromo(palabra):
    contar = round(len(palabra)/2)
    for i in range(contar):
        if (palabra[i] != palabra[-(i+1)]):
            return False

    return True

def contar_palindromos(text):
    lista_palabras = text.lower()
    lista_palabras = lista_palabras.replace(".", "").replace(",", "").replace(":", "").replace(";", "")
    lista_palabras = lista_palabras.split()
    lista_palindromos = []

    for palabra in lista_palabras:
        if (es_palindromo(palabra)):
            lista_palindromos.append(palabra)

    dic = {}
    for palabra in lista_palindromos:
        if (not (palabra in dic)):
            dic[palabra] = lista_palindromos.count(palabra)

    return dic



"""Ejercicio 2
Crea una función que reciba dos strings y devuelva un nuevo 
string que sea el resultado de intercalar los caracteres de 
ambos strings de manera alternativa, comenzando con el primer 
carácter del string más largo. Si un string es más largo que el 
otro, los caracteres sobrantes se añaden al final."""

def intercalar_strings (texto1,texto2):
    minimo = min(len(texto1),len(texto2))

    if minimo == len(texto2):
        str1 = texto1
        str2 = texto2
    else:
        str1 = texto2
        str2 = texto1

    nuevo_string = ""

    for i in range(minimo):
        nuevo_string += f"{str1[i]}{str2[i]}"

    str1 = str1[minimo:]
    str2 = str2[minimo:]

    nuevo_string += f"{str1}{str2}"
    return nuevo_string

 

"""Ejercicio 3
Crea una función que reciba un string con fechas en formato 
"DD/MM/YYYY" y devuelva un nuevo string donde todas las fechas 
estén convertidas al formato "YYYY-MM-DD". Las fechas pueden 
parecer en cualquier parte del texto y estar separadas por 
cualquier caracter no numérico."""

import re

def convertir_fechas(texto):
    return re.sub(
        r'\b(\d{2})/(\d{2})/(\d{4})\b',
        lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)}",
        texto
    )

