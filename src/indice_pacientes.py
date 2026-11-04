class IndicePacientes:
    def __init__(self):
        self._por_codigo = {}

    def agregar(self, paciente):
        if paciente.codigo in self._por_codigo:
            raise ValueError(f"Paciente duplicado: {paciente.codigo}")
        self._por_codigo[paciente.codigo] = paciente

    def buscar(self, codigo):
        if codigo not in self._por_codigo:
            raise KeyError(f"No existe paciente con código {codigo}")
        return self._por_codigo[codigo]

    def existe(self, codigo):
        return codigo in self._por_codigo

    def __len__(self):
        return len(self._por_codigo)

    def __repr__(self):
        return f"IndicePacientes({self._por_codigo!r})"