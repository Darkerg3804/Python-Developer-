# EJERCICIO 8 — SETS

# Tienes una tupla de ventas:
# #
# # ventas = (
# #     ("Ana", "arroz"),
# #     ("Luis", "cafe"),
# #     ("Ana", "aceite"),
# #     ("Pedro", "arroz"),
# #     ("Luis", "leche"),
# #     ("Ana", "cafe"),
# # )
# #
# # Escribe una función que devuelva un set con todos los
# # productos diferentes vendidos.
# #
# # Resultado esperado:
# #
# # {"arroz", "cafe", "aceite", "leche"}
# #
# # La función debe recibir la tupla como parámetro.
# 

def productos_vendidos(ventas):
    lista = []
    for i in ventas:
        lista.append(i[1])

    return set(lista)



ventas = (
    ("Ana", "arroz"),
    ("Luis", "cafe"),
    ("Ana", "aceite"),
    ("Pedro", "arroz"),
    ("Luis", "leche"),
    ("Ana", "cafe"),
    )

print(productos_vendidos(ventas))
