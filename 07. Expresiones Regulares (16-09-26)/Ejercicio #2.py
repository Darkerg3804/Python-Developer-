import re
texto = "Python permite programar proyectos grandes y pequeños."
patron = r"\b[Pp]\w*"

coincidencia = re.findall(patron,texto)

print(coincidencia)