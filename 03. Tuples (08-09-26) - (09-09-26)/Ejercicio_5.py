# ============================================================
# EJERCICIO 5 — Transponer una matriz
# ============================================================
# Dada una matriz representada como tupla de tuplas:
#
# matriz = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
#
# Crea una función que devuelva su transpuesta:
#
# (
#     (1, 4, 7),
#     (2, 5, 8),
#     (3, 6, 9)
# )
#
# Intenta hacerlo sin NumPy.
#
# La función debe funcionar para cualquier matriz rectangular
# válida, no solamente para una matriz 3x3.


def matriz_transpuesta(matriz):
    
    nuevamatriz = []

    for i in range(len(matriz[0])):
        lista = []
        for j in range(len(matriz)):
            lista.append(matriz[j][i])
        nuevamatriz.append(tuple(lista))

    return tuple(nuevamatriz)

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
    )

traspuesta = matriz_transpuesta(matriz)

for i in traspuesta:
    print(i)