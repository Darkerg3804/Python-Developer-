def Procesamiento_ventas (venta):
    dic1 = {}
    

    for i in range(len(venta)):
        if not(venta[i][0] in dic1):
            dic1[venta[i][0]] = venta[i][2] * venta[i][3]
        else:
            dic1[venta[i][0]] += venta[i][2] * venta[i][3]

    nuevatupla = []


    for i in dic1:
        dic2 = {}
        ganador = ""
        for j in venta:
            if i == j[0]:
                if not(j[1] in dic2):
                    dic2[j[1]] = j[2]
                else:
                    dic2[j[1]] += j[2]

        ganador = max(dic2, key=dic2.get)

        nuevatupla.append((i,dic1[i],ganador))

    if __name__ == "__main__":
        print(tuple)

    
    return tuple(nuevatupla)

if __name__ == "__main__":
    from datos import ventas

    print(Procesamiento_ventas(ventas))