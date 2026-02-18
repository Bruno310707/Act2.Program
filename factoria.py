import re
import pdfplumber
from Universidad import Universidad
from Departamento import Departamento

class Factoria:
    @staticmethod
    def construir_universidad_desde_pdf(ruta_pdf):
        # 1. Creamos la instancia de la Universidad
        uni = Universidad("Universidad de Sevilla")
        contador_deptos = 0
        
        # 2. Preparamos el patrón para identificar líneas válidas.
        # Busca "DEPARTAMENTO DE " seguido de texto, y luego captura 5 bloques de números.
        patron = re.compile(r"^(DEPARTAMENTO DE .*?)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\d\.,]+)$")

        # Función auxiliar para convertir texto tipo "1.479,36" a float de Python (1479.36)
        def parsear_numero(cadena):
            # Quitamos el punto de los miles y cambiamos la coma decimal por un punto
            cadena_limpia = cadena.replace('.', '').replace(',', '.')
            return float(cadena_limpia)

        # 3. Extraemos el texto del PDF
        try:
            with pdfplumber.open(ruta_pdf) as pdf:
                for pagina in pdf.pages:
                    texto = pagina.extract_text()
                    
                    if not texto:
                        continue
                    
                    # Leemos línea a línea
                    for linea in texto.split('\n'):
                        linea = linea.strip()
                        
                        # Filtramos solo las líneas que nos interesan
                        if linea.startswith("DEPARTAMENTO DE"):
                            match = patron.match(linea)
                            if match:
                                nombre = match.group(1).strip()
                                etc = parsear_numero(match.group(2))
                                prof_tc = parsear_numero(match.group(3))
                                prof_tp = parsear_numero(match.group(4))
                                # El grupo 5 es el total de profesores del PDF, pero lo ignoramos 
                                # porque nuestro objeto 'Departamento' ya lo calcula internamente.
                                experimentalidad = parsear_numero(match.group(6))
                                
                                # Instanciamos y añadimos a la universidad
                                nuevo_depto = Departamento(nombre, etc, prof_tc, prof_tp, experimentalidad)
                                uni.departamentos.append(nuevo_depto)
                                contador_deptos += 1
                            else:
                                print(f"-> Ojo, la línea empieza por 'DEPARTAMENTO DE' pero el formato no encaja: {linea}")
                                
        except FileNotFoundError:
            print(f"Error: No se ha encontrado el archivo '{ruta_pdf}'. Comprueba la ruta.")
            return None

        # 4. Control de calidad final (verificación de 134 filas)
        print("-" * 50)
        if contador_deptos == 134:
            print(f"✅ ¡Éxito! Se han extraído exactamente {contador_deptos} departamentos.")
        else:
            print(f"❌ ¡ALERTA! Se han extraído {contador_deptos} departamentos, pero el boletín exige 134.")
            print("Revisa el PDF, puede que algún departamento ocupe dos líneas o tenga un formato raro.")
        print("-" * 50)
        
        return uni
    
    # --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # Sustituye 'departamentos.pdf' por la ruta real si está en otra carpeta
    mi_universidad = Factoria.construir_universidad_desde_pdf('departamentos.pdf')
    
    # Para comprobar que los datos entraron bien (opcional):
    if mi_universidad and len(mi_universidad.departamentos) > 0:
        primer_depto = mi_universidad.departamentos[0]
        print(f"\nPrueba del primer registro:")
        print(f"Nombre: {primer_depto.nombre}")
        print(f"Carga docente real: {primer_depto.calcular_carga_docente_real():.2f}")