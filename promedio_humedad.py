with open("datos.txt", "r") as f:
    datos = f.readlines()
    i = 6
    lista_humedades = list()
    for letras in datos[i]:
        lista_humedades.append(float(datos[i][8:13]))
        i += 10

        if i == 106:
            break

promedio_humedades = sum(lista_humedades)/len(lista_humedades)
print(lista_humedades)
print(promedio_humedades)