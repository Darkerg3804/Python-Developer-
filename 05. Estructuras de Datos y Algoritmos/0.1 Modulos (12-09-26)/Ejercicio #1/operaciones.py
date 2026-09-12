def suma(a,b):
    return a+b

def resta(a,b):
    return a - b

def producto(a,b):
    return a*b

def divisor(a,b):
    if b == 0:
        return "Division por 0"
    else:
        return a/b

def potencia(a,b):
    if b == 0:
        return 1

    inverso = False

    if b < 0:
        b = b * (-1)
        inverso = True

    resultado = 1

    for i in range (b):
        resultado = resultado * a

    if inverso:
        return (1/resultado)
    else:
        return resultado

def raiz(a,b):
    if a < 0:
        return "error de dominio"
    if a == 0:
        return 0 
    
    if not(b.is_integer()):
        return "error de funcion" # aun la funcion no lo contempla

    inverso = False
    
    x_1 = a
    x_0 = 0


    if b < 0:
        b = b* (-1)
        inverso = True

    while(abs(x_1 - x_0) > 0.0000001):
        x_0 = x_1
        x_1 = x_0 - (potencia(x_0,b) - a)/(x_0 * potencia(x_0,b-1))

    x_1 = round(x_1,4)

    if inverso:
        return 1 / x_1
    else:
        return x_1


    