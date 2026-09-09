# ============================================================
# EJERCICIO 1 — Desempaquetado y transformación
# ============================================================
# Dada una tupla de registros:
#
# personas = (
#     ("Ana", 25, "Santo Domingo"),
#     ("Luis", 31, "Santiago"),
#     ("Pedro", 19, "La Vega"),
#     ("Marta", 42, "Santo Domingo")
# )
#
# Crea una función que devuelva una tupla donde cada registro
# tenga solamente:
#
# (nombre, edad)
#
# Resultado:
# (
#     ("Ana", 25),
#     ("Luis", 31),
#     ("Pedro", 19),
#     ("Marta", 42)
# )
#
# Debes desempaquetar cada registro.

def cambiarPersona(tupla):
    lista = []
    for persona in tupla:
        lista.append((persona[0],persona[1]))

    return tuple(lista)

personas = (
    ("Ana", 25, "Santo Domingo"),
    ("Luis", 31, "Santiago"),
    ("Pedro", 19, "La Vega"),
    ("Marta", 42, "Santo Domingo")
    )

nuevapersona = cambiarPersona(personas)

print(nuevapersona)