import ArbolBinario as AB
# Crear el árbol
arbol = AB.BSTUsuarios()

# Insertar usuarios (desordenados, el árbol se ordena solo)
datos = [
    (45, "Ana"),
    (12, "Luis"),
    (78, "Marta"),
    (3, "Pedro"),
    (99, "Sofía"),
    (23, "Carlos"),
    (67, "Elena"),
    (8, "Diego"),
]

for id, nombre in datos:
    arbol.insertar(id, nombre)

# 1. Buscar un usuario por ID
print("Buscar 45:", arbol.buscar(45))    # Ana
print("Buscar 99:", arbol.buscar(99))    # Sofía
print("Buscar 50:", arbol.buscar(50))    # None

# 2. Consultar por rango: IDs entre 20 y 70
print("\nIDs entre 20 y 70:")
for id, nombre in arbol.rango(20, 70):
    print(f"  {id}: {nombre}")
# 23: Carlos
# 45: Ana
# 67: Elena

# 3. Mínimo y máximo
print("\nMínimo:", arbol.minimo())   # (3, 'Pedro')
print("Máximo:", arbol.maximo())     # (99, 'Sofía')

# 4. Recorrido ordenado
print("\nTodos ordenados por ID:")
for id, nombre in arbol.in_order():
    print(f"  {id}: {nombre}")
# 3: Pedro
# 8: Diego
# 12: Luis
# 23: Carlos
# 45: Ana
# 67: Elena
# 78: Marta
# 99: Sofía