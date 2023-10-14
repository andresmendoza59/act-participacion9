with open("datos.txt", "r") as f:
    datos = f.readlines()
    i = 5
    lista_temperaturas = list()
    for letras in datos[i]:
        lista_temperaturas.append(float(datos[i][13:17]))
        i += 10

        if i == 105:
            break

print(lista_temperaturas)
promedio_temperaturas= sum(lista_temperaturas)/len(lista_temperaturas)