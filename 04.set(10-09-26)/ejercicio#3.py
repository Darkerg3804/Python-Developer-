# EJERCICIO 3 — SETS

# Dados dos sets A y B, devuelve los elementos que pertenecen
# # a A pero no pertenecen a B.
# #
# # Ejemplo:
# #
# # A = {"arroz", "cafe", "aceite", "leche"}
# # B = {"cafe", "leche", "azucar"}
# #
# # salida:
# # {"arroz", "aceite"}
# #
# # El resultado debe ser un nuevo set.
# 

A = {"arroz", "cafe", "aceite", "leche"}
B = {"cafe", "leche", "azucar"}

C = A-B

print(C)