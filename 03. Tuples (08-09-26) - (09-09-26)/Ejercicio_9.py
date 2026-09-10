# ============================================================
# EJERCICIO 9 — Ventana deslizante
# ============================================================
# Dada:
#
# numeros = (1, 4, 7, 2, 9, 3, 8, 5)
#
# Crea una función que reciba la tupla y un tamaño N y devuelva
# todas las ventanas consecutivas de tamaño N.
#
# Ejemplo con N = 3:
#
# (
#     (1, 4, 7),
#     (4, 7, 2),
#     (7, 2, 9),
#     (2, 9, 3),
#     (9, 3, 8),
#     (3, 8, 5)
# )
#
# No uses librerías externas.

def ventanadeslizante (num,N):
    if N <= 0:
        return None
    
    if N >= len(num):
        return num
    
    nuevatupla = []

    for i in range(len(num) - (N-1)):
        lista = []

        for j in range(N):
            lista.append(num[i+j])

        nuevatupla.append(tuple(lista))

    return tuple(nuevatupla)

numeros = (1, 4, 7, 2, 9, 3, 8, 5)

ventana = ventanadeslizante(numeros,3)

for elemento in ventana:
    print(elemento)