# EJERCICIO 4 — SETS

# Dados dos sets que representan estudiantes inscritos en
# # dos materias:
# #
# # matematicas = {...}
# # programacion = {...}
# #
# # Obtén:
# #
# # 1. Estudiantes inscritos en ambas materias.
# # 2. Estudiantes inscritos solamente en matemáticas.
# # 3. Estudiantes inscritos solamente en programación.
# # 4. Estudiantes inscritos en al menos una de las dos materias.
# #
# # Devuelve los cuatro resultados.
# 

matematicas = {"Ana", "Luis", "Carlos", "Sofia", "Pedro"}
programacion = {"Ana", "Luis", "Elena", "Miguel", "Sofia"}

Ambas = matematicas&programacion
SoloMatematicas = matematicas - programacion
soloProgramacion = programacion -matematicas
enSolo1 = matematicas ^ programacion
todos = matematicas | programacion

print(f"1. Estudiantes inscritos en ambas materias: {Ambas}" )
print(f"2. Estudiantes inscritos solamente en matemáticas: {SoloMatematicas}" )
print(f"3. Estudiantes inscritos solamente en programación: {soloProgramacion}" )
print(f"4. Estudiantes inscritos en solo 1 materia: {enSolo1}" )
print(f"5. Estudiantes inscritos en al menos una de las dos materias: {todos}" )

