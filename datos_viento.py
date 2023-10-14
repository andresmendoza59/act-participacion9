# Diccionario de direcciones y sus grados correspondientes
direcciones_grados = {
    "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
    "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
    "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
    "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
}

suma_velocidades = 0
direcciones = []

# Datos estaciones
estaciones = [
    {"nombre": "Aeropuerto Internacional", "Viento": "14.5,ESE"},
    {"nombre": "Centro Historico", "Viento": "12.8,N"},
    {"nombre": "Coyoacan", "Viento": "10.2,S"},
    {"nombre": "Polanco", "Viento": "8.9,NE"},
    {"nombre": "Xochimilco", "Viento": "11.1,W"},
    {"nombre": "Santa Fe", "Viento": "7.6,NW"},
    {"nombre": "Ciudad Universitaria", "Viento": "6.2,SW"},
    {"nombre": "Reforma", "Viento": "9.8,E"},
    {"nombre": "Tlalpan", "Viento": "12.1,SE"},
    {"nombre": "Cuajimalpa", "Viento": "5.2,ENE"}
]

for estacion in estaciones:
    viento_info = estacion["Viento"].split(",")
    velocidad = float(viento_info[0])
    direccion = viento_info[1]

    suma_velocidades += velocidad
    direcciones.append(direccion)

# Calcular velocidad promedio
velocidad_promedio = suma_velocidades / len(estaciones)

# Calcular dirección predominante
grados_promedio = sum(direcciones_grados[direccion] for direccion in direcciones) / len(estaciones)

# Convertir el promedio de grados nuevamente a una dirección
for direccion, grados in direcciones_grados.items():
    if grados_promedio <= grados + 11.25:
        direccion_predominante = direccion
        break

print(f"Velocidad promedio del viento: {velocidad_promedio}")
print(f"Dirección predominante del viento: {direccion_predominante}")