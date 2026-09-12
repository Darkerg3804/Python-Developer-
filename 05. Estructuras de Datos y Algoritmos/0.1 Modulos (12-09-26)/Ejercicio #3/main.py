from funciones import Procesamiento_ventas
from datos import ventas

procesadas = Procesamiento_ventas(ventas)

for i in procesadas:
    print(i) 

