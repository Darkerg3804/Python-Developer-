# EJERCICIO 5 — SETS


# Escribe una función que determine si todos los elementos de
# # un set A también pertenecen a un set B.
# #
# # Ejemplo:
# #
# # A = {2, 4}
# # B = {1, 2, 3, 4, 5}
# #
# # salida:
# # True
# #
# # Pero:
# #
# # A = {2, 7}
# # B = {1, 2, 3, 4, 5}
# #
# # salida:
# # False
# #
# # No recorras manualmente todos los elementos para resolverlo.
# # Utiliza la operación apropiada de conjuntos.
# 

A = {2, 7}
B = {1, 2, 3, 4, 5}

C = A <= B

print(f"A es subconjunto de B: {C}")