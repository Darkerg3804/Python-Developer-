# ============================================================
# EJERCICIO 2 — Filtrar registros
# ============================================================
# Usando la misma estructura anterior, crea una función que
# reciba:
#
# - la tupla de personas
# - una edad mínima
#
# y devuelva únicamente las personas cuya edad sea >= edad mínima.
#
# Ejemplo:
#
# edad_minima = 30
#
# Resultado:
# (
#     ("Luis", 31, "Santiago"),
#     ("Marta", 42, "Santo Domingo")
# )

def filtrar_edad_minima(tupla,edadmin):
    lista = []
    for persona in tupla:
        if persona[1] >= edadmin:
            lista.append(persona)

    return tuple(lista)


personas = (
    ("Ana", 25, "Santo Domingo"),
    ("Luis", 31, "Santiago"),
    ("Pedro", 19, "La Vega"),
    ("Marta", 42, "Santo Domingo")
    )

print(filtrar_edad_minima(personas,20))