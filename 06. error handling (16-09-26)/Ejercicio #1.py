#Ejercicio 1 — Conversión segura de números
#Pide al usuario un número entero y muéstralo multiplicado por 2. 
#Si escribe algo que no es un número, muestra un mensaje de error 
#en vez de que el programa explote.

valor_input = input("Introduzca un numero entero: ")

try:
    valor_input = int(valor_input)

except ValueError:
    print(f"El valor {valor_input} no es un entero")

else:
    valor_input = valor_input * 2 
    print(f"resultado :{valor_input}")
