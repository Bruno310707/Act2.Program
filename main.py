import re
import pdfplumber
from Universidad import Universidad
from Departamento import Departamento
from factoria import Factoria

if __name__ == "__main__":
    
    print("Leyendo PDF y construyendo la universidad...\n")
    # Construimos el objeto usando la factoría
    mi_u = Factoria.construir_universidad_desde_pdf('departamentos.pdf')
    
    if mi_u and len(mi_u.departamentos) > 0:
        N = 5  # Cambia esto si quieres ver un top 3 o un top 10
        
        print("\n" + "="*50)
        print(f" RESULTADOS: {mi_u.nombre} ".center(50, "="))
        print("="*50)

        # 1º) n departamentos con mayor carga
        print(f"\n[1] TOP {N} MAYOR CARGA DOCENTE:")
        for d in mi_u.obtener_top_n_mayor_carga(N):
            print(f"    - {d.nombre}: {d.calcular_carga_docente_real():.2f}")

        # 2º) n departamentos con menor carga
        print(f"\n[2] TOP {N} MENOR CARGA DOCENTE:")
        for d in mi_u.obtener_top_n_menor_carga(N):
            print(f"    - {d.nombre}: {d.calcular_carga_docente_real():.2f}")

        # 3º) Diccionario cantidad departamentos por coeficiente
        print("\n[3] DEPARTAMENTOS POR COEFICIENTE DE EXPERIMENTALIDAD:")
        conteo_exp = mi_u.contar_por_experimentalidad()
        for coef, cantidad in conteo_exp.items():
            print(f"    - Coef. {coef}: {cantidad} departamentos")

        # 4º) Diccionario media de carga por coeficiente
        print("\n[4] MEDIA DE CARGA DOCENTE POR COEFICIENTE:")
        medias_exp = mi_u.media_carga_por_experimentalidad()
        for coef, media in medias_exp.items():
            print(f"    - Coef. {coef}: {media:.2f} (media)")

        # 5º) Extremos (Mayor y menor)
        print("\n[5] EXTREMOS DE MEDIA DE CARGA:")
        c_mayor, c_menor = mi_u.extremos_media_carga_experimentalidad()
        print(f"    - Mayor media: Coef. {c_mayor} (Media: {medias_exp[c_mayor]:.2f})")
        print(f"    - Menor media: Coef. {c_menor} (Media: {medias_exp[c_menor]:.2f})")
        
        print("\n" + "="*50)