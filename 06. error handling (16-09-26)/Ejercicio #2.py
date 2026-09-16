#Ejercicio 2 — División con dos errores posibles
#Pide dos números y divide el primero entre el segundo. Maneja por separado:
#Que no sean números (ValueError)
# Que el segundo sea cero (ZeroDivisionError)

Valor_1 = input("Introduzca el Numerador: ")
valor_2 = input("Introduzca el Denominador: ")

try:
    Valor_1 = float(Valor_1)
    valor_2 = float(valor_2)
    print(f"El Resultado de la division es: {Valor_1 / valor_2}")

except ValueError:
    print(f"tus valores no son ambos numeros: {Valor_1} , {valor_2}")

except ZeroDivisionError:
    print("No se puede dividir por Zero")

