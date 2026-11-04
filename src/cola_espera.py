class ColaEspera:
    def __init__(self):
        self._pacientes = []

    def encolar(self, paciente):
        self._pacientes.append(paciente)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("No hay pacientes en espera")
        return self._pacientes.pop(0)

    def siguiente(self):
        if self.esta_vacia():
            raise ValueError("No hay pacientes en espera")
        return self._pacientes[0]

    def esta_vacia(self):
        return len(self._pacientes) == 0

    def __len__(self):
        return len(self._pacientes)

    def __repr__(self):
        return f"ColaEspera({self._pacientes!r})"