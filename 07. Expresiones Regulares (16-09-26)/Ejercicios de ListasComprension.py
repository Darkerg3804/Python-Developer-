# ============================================
# EJERCICIOS: LIST COMPREHENSIONS
# Escribe la solución debajo de cada enunciado.
# ============================================

# 1. Lista con los cuadrados de los números del 1 al 15.
#    Resultado esperado: [1, 4, 9, ..., 225]
lista_1 = [x**2 for x in range(1,15+1)]


# 2. Lista con los números pares del 1 al 30.
#    Resultado esperado: [2, 4, 6, ..., 30]
lista_2 = [x for x in range(31) if (x % 2 == 0)]

# 3. Lista con las primeras letras de cada palabra en "python es genial para aprender".
#    Resultado esperado: ['p', 'e', 'g', 'p', 'a']
lista_3 = [palabra[0] for palabra in ("python es genial para aprender").split()]



# 4. Lista con las palabras de la frase "el rápido zorro marrón salta sobre el perro" que tengan más de 4 letras.
#    Resultado esperado: ['rápido', 'marrón', 'salta', 'sobre', 'perro']
lista_4 = [palabra for palabra in ("el rápido zorro marrón salta sobre el perro").split() if len(palabra >4 )]

# 5. Lista con las longitudes de cada palabra en "uno dos tres cuatro".
#    Resultado esperado: [3, 3, 4, 6]
lista_5 = [len(palabra) for palabra in ("uno dos tres cuatro").split()]

# 6. Lista con los números del 1 al 50 que sean divisibles por 3 o por 5.
#    Resultado esperado: [3, 5, 6, 9, 10, 12, ..., 50]
lista_6 = [x for x in range(1,50+1) if ((x % 3) ==0) or ((x % 5) == 0)]

# 7. Lista con los números del 1 al 20 elevados al cubo, pero solo los impares.
#    Resultado esperado: [1, 27, 125, ..., 6859]
lista_7 = [x**3 for x in range(1,20+1) if ((x % 2) != 0)]

# 8. Aplanar la matriz [[1, 2, 3], [4, 5], [6, 7, 8, 9]] en una sola lista.
#    Resultado esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[1, 2, 3], 
          [4, 5], 
          [6, 7, 8, 9]]

lista_8 = [j for i in matriz for j in i]



# 9. Lista con "par" o "impar" según corresponda, para los números del 0 al 9.
#    Resultado esperado: ['par', 'impar', 'par', 'impar', ...]
lista_9 = ["par" if (i % 2) == 0 else "impar" for i in range(0,10)]

# 10. Lista con tuplas (número, cuadrado) para los números del 1 al 5.
#     Resultado esperado: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
lista_10 = [(i,i**2) for i in range(1,6)]
