with open("datos.txt", "r") as f:
    datos = f.readlines()
    i = 7
    lista_presiones = list()
    for letras in datos[i]:
        lista_presiones.append(float(datos[i][8:15]))
        i += 10

        if i == 107:
            break

promedio_presiones = sum(lista_presiones)/len(lista_presiones)
print(lista_presiones)
print(promedio_presiones)