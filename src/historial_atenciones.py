class Atencion:
    def __init__(self, codigo_paciente, descripcion):
        self.codigo_paciente = codigo_paciente
        self.descripcion = descripcion

    def __repr__(self):
        return f"Atencion({self.codigo_paciente!r}, {self.descripcion!r})"


class HistorialAtenciones:
    def __init__(self):
        self._atenciones = []

    def registrar(self, codigo_paciente, descripcion):
        self._atenciones.append(Atencion(codigo_paciente, descripcion))

    def obtener(self, codigo_paciente):
        return [a for a in self._atenciones if a.codigo_paciente == codigo_paciente]

    def __len__(self):
        return len(self._atenciones)

    def __repr__(self):
        return f"HistorialAtenciones({self._atenciones!r})"