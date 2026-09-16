#Ejercicio 3 — Acceso seguro a una lista
#Dada esta lista frutas = ["manzana", "pera", "uva"],
#pide un índice al usuario y muestra la fruta correspondiente.
#Si el índice está fuera de rango, avisa. Además, usa finally 
#para imprimir "Fin del programa" siempre.

frutas = ["manzana", "pera", "uva", "mango", "melocoton", "sandia"]

print("Seleccione la fruta: ")

for i, fruta in enumerate(frutas):
    print(f"{i} - {fruta}")

valor_usuario = input("Introduzca un indice: ")

try:
    valor_usuario = int(valor_usuario)
    if valor_usuario < 0:
        raise IndexError
    print(f"Su fruta es: {frutas[valor_usuario]}")
except ValueError:
    print("No selecciono un entero")
except IndexError:
    print("Debe seleccionar un numero valido")

finally:
    print("Fin del programa")