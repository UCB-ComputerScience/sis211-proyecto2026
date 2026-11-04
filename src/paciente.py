# Renombren esta clase al concepto de su caso (Paciente, Pedido, Pelicula…).
# No implementen pila, cola ni hash aquí: eso va en otras clases cuando codeen.


class Paciente:
    def __init__(self, codigo, nombre, ci=None, prioridad=3):
        self.codigo = codigo
        self.nombre = nombre
        self.ci = ci
        # 1 = crítico, 2 = grave, 3 = normal, 4 = leve, 5 = mínimo
        self.prioridad = prioridad

    def __repr__(self):
        return (
            f"Paciente(codigo={self.codigo!r}, nombre={self.nombre!r}, "
            f"ci={self.ci!r}, prioridad={self.prioridad})"
        )