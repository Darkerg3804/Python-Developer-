# ============================================================
# EJERCICIO 3 — Ordenar sin modificar la tupla original
# ============================================================
# Dada:
#
# productos = (
#     ("Arroz", 65),
#     ("Aceite", 180),
#     ("Habichuela", 120),
#     ("Leche", 75),
#     ("Café", 250)
# )
#
# Devuelve una nueva tupla con los productos ordenados
# de menor a mayor precio.
#
# NO uses sorted().
#
# La tupla original debe permanecer intacta.
#
# Resultado esperado:
#
# (
#     ("Arroz", 65),
#     ("Leche", 75),
#     ("Habichuela", 120),
#     ("Aceite", 180),
#     ("Café", 250)
# )

def burblesort (lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j][1] > lista[j+1][1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista
                


def ordenar_tupla_porPrecio(tupla):

    listaproducto = []

    for producto in tupla:
        listaproducto.append(producto)

    return tuple(burblesort(listaproducto))
    
productos = (
    ("Arroz", 65),
    ("Aceite", 180),
    ("Habichuela", 120),
    ("Leche", 75),
    ("Café", 250) 
    )

productosordenados = ordenar_tupla_porPrecio(productos)

for i in productosordenados:
    print(i)
