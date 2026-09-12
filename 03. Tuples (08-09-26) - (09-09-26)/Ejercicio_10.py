# ============================================================
# EJERCICIO 10 — Procesamiento completo de datos
# ============================================================
# Tienes registros de ventas:
#
# ventas = (
#     ("Ana", "arroz", 3, 65),
#     ("Luis", "cafe", 2, 250),
#     ("Ana", "aceite", 1, 180),
#     ("Pedro", "arroz", 5, 65),
#     ("Luis", "arroz", 2, 65),
#     ("Ana", "cafe", 1, 250),
#     ("Pedro", "aceite", 2, 180),
#     ("Luis", "cafe", 3, 250)
# )
#
# Cada registro contiene:
#
# (cliente, producto, cantidad, precio_unitario)
#
# Crea una función que devuelva una estructura que indique,
# para cada cliente:
#
# - cuánto dinero gastó en total
# - cuál fue su producto más comprado en cantidad
#
# Ejemplo conceptual:
#
# (
#     ("Ana", 625, "cafe"),
#     ("Luis", 1120, "cafe"),
#     ("Pedro", 685, "arroz")
# )
#
# No importa si eliges otra estructura de salida mientras
# contenga correctamente la información.
#
# IMPORTANTE:
# Debes recorrer las ventas y construir la información tú mismo.
# No uses pandas ni Counter.

def Procesamiento_ventas (venta):
    dic1 = {}
    

    for i in range(len(ventas)):
        if not(venta[i][0] in dic1):
            dic1[venta[i][0]] = venta[i][2] * venta[i][3]
        else:
            dic1[venta[i][0]] += venta[i][2] * venta[i][3]

    nuevatupla = []


    for i in dic1:
        dic2 = {}
        ganador = ""
        for j in ventas:
            if i == j[0]:
                if not(j[1] in dic2):
                    dic2[j[1]] = j[2]
                else:
                    dic2[j[1]] += j[2]

        ganador = max(dic2, key=dic2.get)

        nuevatupla.append((i,dic1[i],ganador))

    
    return tuple(nuevatupla)

    
    

ventas = (
    ("Ana", "arroz", 3, 65),
    ("Luis", "cafe", 2, 250),
    ("Ana", "aceite", 1, 180),
    ("Pedro", "arroz", 5, 65),
    ("Luis", "arroz", 2, 65),
    ("Ana", "cafe", 1, 250),
    ("Pedro", "aceite", 2, 180),
    ("Luis", "cafe", 3, 250)
)

procesadas = Procesamiento_ventas(ventas)

for i in procesadas:
    print(i) 