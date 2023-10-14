from promedio_temperatura import promedio_temperaturas
from promedio_humedad import promedio_humedades
from promedio_presion import promedio_presiones
from datos_viento import velocidad_promedio, direccion_predominante

class DatosMetereologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:

        return promedio_temperaturas, promedio_humedades, promedio_presiones, velocidad_promedio, direccion_predominante
    
datos_metereologicos = DatosMetereologicos("datos.txt")
print(datos_metereologicos.procesar_datos())