import pdfplumber
import re

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    # 1º) n departamentos con MAYOR carga docente real
    def obtener_top_n_mayor_carga(self, n):
        ordenados = sorted(self.departamentos, 
                           key=lambda d: d.calcular_carga_docente_real(), 
                           reverse=True)
        return ordenados[:n]

    # 2º) n departamentos con MENOR carga docente real
    def obtener_top_n_menor_carga(self, n):
        ordenados = sorted(self.departamentos, 
                           key=lambda d: d.calcular_carga_docente_real())
        return ordenados[:n]

    # 3º) Diccionario con el número de departamentos por cada coeficiente
    def contar_por_experimentalidad(self):
        conteo = {}
        for depto in self.departamentos:
            coef = depto.experimentalidad
            conteo[coef] = conteo.get(coef, 0) + 1
        return conteo

    # 4º) Diccionario con la media de carga docente real por cada coeficiente
    def media_carga_por_experimentalidad(self):
        suma_cargas = {}
        conteo = self.contar_por_experimentalidad() 
        # Sumamos todas las cargas por coeficiente
        for depto in self.departamentos:
            coef = depto.experimentalidad
            carga = depto.calcular_carga_docente_real()
            suma_cargas[coef] = suma_cargas.get(coef, 0) + carga

        # Calculamos la media (Suma total / Cantidad de departamentos)
        medias = {}
        for coef in suma_cargas:
            medias[coef] = suma_cargas[coef] / conteo[coef]
            
        return medias

    # 5º) Los coeficientes con mayor y menor media de carga
    def extremos_media_carga_experimentalidad(self):
        # Obtenemos el diccionario del método 4
        medias = self.media_carga_por_experimentalidad()
        
        if not medias:
            return None, None

        # max() y min() pueden buscar el valor más alto/bajo de un diccionario usando '.get'
        coef_mayor = max(medias, key=medias.get)
        coef_menor = min(medias, key=medias.get)
        
        return coef_mayor, coef_menor





