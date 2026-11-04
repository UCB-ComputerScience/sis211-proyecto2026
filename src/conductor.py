class Conductor:
    """Un conductor identificado por su código."""
 
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True
        self.viajes = 0
 
    def __repr__(self):
        estado = "disponible" if self.disponible else "ocupado"
        return f"Conductor({self.codigo}, {self.nombre}, {estado})"
 