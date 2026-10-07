# Renombren esta clase al concepto de su caso (Paciente, Pedido, Pelicula…).
# No implementen pila, cola ni hash aquí: eso va en otras clases cuando codeen.


class Paciente:
    def __init__(self, codigo, nombre, ci=None):
        self.codigo = codigo
        self.nombre = nombre
        self.ci = ci

    def __repr__(self):
        return f"Paciente(codigo={self.codigo!r}, nombre={self.nombre!r}, ci={self.ci!r})"