# EJERCICIO 6 — SETS

# Tienes dos inventarios representados como sets de productos.
# #
# # inventario_A = {...}
# # inventario_B = {...}
# #
# # Determina:
# #
# # 1. Productos que están en A pero no en B.
# # 2. Productos que están en B pero no en A.
# # 3. Productos presentes en ambos.
# #
# # Interpreta el problema como una comparación entre inventarios.
# #
# # Devuelve los tres sets.
# 

inventario_A = {"manzanas", "plátanos", "naranjas", "uvas", "peras", "kiwis"}
inventario_B = {"plátanos", "uvas", "fresas", "sandías", "kiwis", "melocotones"}

print(f"productos de A que no estan en B: {inventario_A - inventario_B}")
print(f"productos de A que no estan en B: {inventario_B - inventario_A}")
print(f"productos de A que no estan en B: {inventario_A & inventario_B}")
