import re

texto = "El gato duerme en el sofá"

busqueda = re.search("duerme", texto)

texto = "Tengo 3 manzanas, 25 naranjas y 100 guineos."

coincidencia = re.findall(r"\d+", texto)
print(coincidencia)
