# ============================================================
# EJERCICIO 4 — Producto más caro de cada categoría
# ============================================================
# Dada:
#
# productos = (
#     ("Arroz", "comida", 65),
#     ("Aceite", "comida", 180),
#     ("Jabón", "limpieza", 75),
#     ("Cloro", "limpieza", 120),
#     ("Café", "comida", 250),
#     ("Detergente", "limpieza", 200)
# )
#
# Devuelve una tupla con el producto más caro de cada categoría.
#
# Resultado:
#
# (
#     ("Café", "comida", 250),
#     ("Detergente", "limpieza", 200)
# )
#
# No sabes de antemano cuáles son las categorías.

def caro_categoria (tupla):
    
    diccategorias = {}
    

    for i in range(len(tupla)):
        
        if not(tupla[i][1] in diccategorias):
            
            diccategorias[tupla[i][1]] = [tupla[i][2],i]
        else:
            if tupla[i][2] > diccategorias[tupla[i][1]][0]:
                diccategorias[tupla[i][1]] = [tupla[i][2] , i]

    neolista = []
    

    for i in diccategorias:
        posicion = diccategorias[i][1]

        neolista.append(tupla[posicion])

    return tuple(neolista)

            
productos = (
    ("Arroz", "comida", 65),
    ("Aceite", "comida", 180),
    ("Jabón", "limpieza", 75),
    ("Cloro", "limpieza", 120),
    ("Café", "comida", 250),
    ("Detergente", "limpieza", 200)
    )

print(caro_categoria(productos))
