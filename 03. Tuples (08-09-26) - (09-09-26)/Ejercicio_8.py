# ============================================================
# EJERCICIO 8 — Intersección por clave
# ============================================================
# Tienes dos conjuntos de registros:
#
# empleados = (
#     (101, "Ana"),
#     (102, "Luis"),
#     (103, "Pedro"),
#     (104, "Marta")
# )
#
# salarios = (
#     (101, 50000),
#     (103, 62000),
#     (104, 55000),
#     (105, 70000)
# )
#
# Une la información usando el ID como clave.
#
# Resultado:
#
# (
#     (101, "Ana", 50000),
#     (103, "Pedro", 62000),
#     (104, "Marta", 55000)
# )
#
# El empleado 102 no aparece porque no tiene salario.
# El salario 105 no aparece porque no existe ese empleado.

def crear_diccionario(inventario):
    dic = {}

    for i in range(len(inventario)):
        
        dic[inventario[i][0]] = inventario[i][1]

    return dic


def agrupar_salario_empleados(tupl_empleados,tupl_salarios):
    dic_empleados = crear_diccionario(tupl_empleados)
    dic_salarios = crear_diccionario(tupl_salarios)

    nuevatupla = []    

    for clave in dic_empleados:
        try:
            nuevatupla.append((clave,dic_empleados[clave],dic_salarios[clave]))
        except:
            nuevatupla.append((clave,dic_empleados[clave],None))

    for clave in dic_salarios:
        if not(clave in dic_empleados):
            nuevatupla.append((clave,"No existe",None))

    return tuple(nuevatupla)




empleados = (
    (101, "Ana"),
    (102, "Luis"),
    (103, "Pedro"),
    (104, "Marta")
    )
salarios = (
    (101, 50000),
    (103, 62000),    
    (104, 55000),
    (105, 70000)
    )

nueva = agrupar_salario_empleados(empleados,salarios)

for i in nueva:
    print(i)