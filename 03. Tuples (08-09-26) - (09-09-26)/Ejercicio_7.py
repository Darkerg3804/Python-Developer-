# ============================================================
# EJERCICIO 7 — Agrupar registros consecutivos
# ============================================================
# Dada:
#
# ventas = (
#     ("arroz", 2),
#     ("arroz", 3),
#     ("aceite", 1),
#     ("aceite", 4),
#     ("aceite", 2),
#     ("cafe", 1),
#     ("arroz", 5)
# )
#
# Agrupa las ventas consecutivas del mismo producto.
#
# Resultado:
#
# (
#     ("arroz", 5),
#     ("aceite", 7),
#     ("cafe", 1),
#     ("arroz", 5)
# )
#
# OJO:
# Los dos grupos de "arroz" NO deben combinarse porque
# no son consecutivos.

def agrupartupla (tupla):

    memoria = None
    nuevatupla = []

    for producto in tupla:
        if memoria == producto[0]:
            nuevatupla[-1][1] += producto[1]
            
        else:
            nuevatupla.append([producto[0],producto[1]])
            memoria = producto[0]

    for i in range(len(nuevatupla)):
        nuevatupla[i] = tuple(nuevatupla[i])

    nuevatupla = tuple(nuevatupla)
    return nuevatupla

ventas = (
    ("arroz", 2),
    ("arroz", 3),
    ("aceite", 1),
    ("aceite", 4),
    ("aceite", 2),
    ("cafe", 1),
    ("arroz", 5)
    )

agruparventas = agrupartupla(ventas)

for producto in agruparventas:
    print(producto)