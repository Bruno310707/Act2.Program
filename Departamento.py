class Departamento:
    def __init__(self, nombre, etc, profesores_tc, profesores_tp, experimentalidad):
        self.nombre = nombre
        self.etc = etc  
        self.profesores_tc = profesores_tc
        self.profesores_tp = profesores_tp
        self.experimentalidad = experimentalidad
        
        self.total_profesores = self.profesores_tc + (0.5 * self.profesores_tp)

    def calcular_carga_docente_real(self):
        if self.total_profesores == 0:
            return 0
        return (self.etc * self.experimentalidad) / self.total_profesores