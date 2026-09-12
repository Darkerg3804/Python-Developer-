# EJERCICIO 9 — SETS
#
# Resuelve el ejercicio debajo.
#
# ------------------------------------------------------------

# Tienes las compras realizadas en dos meses:
# #
# # enero = (
# #     ("Ana", 500),
# #     ("Luis", 300),
# #     ("Pedro", 700),
# #     ("Maria", 200)
# # )
# #
# # febrero = (
# #     ("Luis", 450),
# #     ("Pedro", 600),
# #     ("Carlos", 800),
# #     ("Ana", 300)
# # )
# #
# # Determina qué clientes realizaron compras en ambos meses.
# #
# # Resultado esperado:
# #
# # {"Ana", "Luis", "Pedro"}
# #
# # Utiliza sets para resolver la parte central del problema.
# 

def set_cliente(mes):
    lista = []

    for i in mes:
        lista.append(i[0])

    return set(lista)

enero = (
    ("Ana", 500),
    ("Luis", 300),
    ("Pedro", 700),
    ("Maria", 200)
    )

febrero = (
    ("Luis", 450),
    ("Pedro", 600),
    ("Carlos", 800),
    ("Ana", 300)
    )

set_enero = set_cliente(enero)
set_febrero = set_cliente(febrero)

print(f"Clientes que compraron en enero y febrero: {set_enero & set_febrero}")

