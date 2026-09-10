# ============================================================
# EJERCICIO 6 — Diferencia entre registros
# ============================================================
# Tienes dos tuplas representando inventarios:
#
# inventario_a = (
#     ("arroz", 20),
#     ("aceite", 15),
#     ("cafe", 8),
#     ("leche", 12)
# )
#
# inventario_b = (
#     ("arroz", 15),
#     ("aceite", 20),
#     ("cafe", 8),
#     ("leche", 5)
# )
#
# Crea una función que compare ambos inventarios y devuelva
# una tupla con:
#
# (producto, diferencia)
#
# solamente para aquellos productos cuya cantidad haya cambiado.
#
# Resultado:
#
# (
#     ("arroz", 5),
#     ("aceite", -5),
#     ("leche", 7)
# )
#
# Convención:
# diferencia = inventario_a - inventario_b

def crear_diccionario(inventario):
    dic = {}

    for i in range(len(inventario)):
        
        dic[inventario[i][0]] = inventario[i][1]

    return dic

def diferencia_inventario(inv_A,inv_B):
    dicA = crear_diccionario(inv_A)
    dicB = crear_diccionario(inv_B)
    
    lista_diferencia = []

    for i in dicA:
    
        diferencia = dicA[i] - dicB[i]
        if diferencia != 0:
            lista_diferencia.append((i,diferencia))

    return tuple(lista_diferencia)


inventario_a = (
    ("arroz", 20),
    ("aceite", 15),
    ("cafe", 8),
    ("leche", 12)
    )

inventario_b = (
    ("arroz", 15),
    ("aceite", 20),
    ("cafe", 8),
    ("leche", 5)
    )

diferencia = diferencia_inventario(inventario_a,inventario_b)

for i in diferencia:
    print(i)