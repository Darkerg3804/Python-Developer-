import re
import random
import string

PATRON = r"^[A-Z]{3}-\d{4}$"

def generar_codigo():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return f"{letras}-{numeros}"

def generar_codigo_valido():
    """Genera hasta obtener uno que cumpla el patrón"""
    while True:
        codigo = generar_codigo()
        if re.match(PATRON, codigo):
            return codigo

for _ in range(5):
    print(generar_codigo_valido())