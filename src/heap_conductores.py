class HeapConductores:
    """Min-heap de conductores ordenado por viajes completados."""

    def __init__(self):
        self._datos = []  # lista de tuplas (viajes, codigo, conductor)

    def esta_vacio(self):
        return len(self._datos) == 0

    def insertar(self, conductor):
        self._datos.append((conductor.viajes, conductor.codigo, conductor))
        self._subir(len(self._datos) - 1)

    def eliminar(self, conductor):
        for i, (_, _, actual) in enumerate(self._datos):
            if actual is conductor:
                ultimo = self._datos.pop()
                if i < len(self._datos):
                    self._datos[i] = ultimo
                    padre = (i - 1) // 2
                    if i > 0 and self._datos[i][:2] < self._datos[padre][:2]:
                        self._subir(i)
                    else:
                        self._bajar(i)
                return

    def extraer(self):
        if self.esta_vacio():
            return None  # caso límite: vacío
        menor = self._datos[0]
        ultimo = self._datos.pop()
        if self._datos:
            self._datos[0] = ultimo
            self._bajar(0)
        return menor[2]

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._datos[i][:2] < self._datos[padre][:2]:
                self._datos[i], self._datos[padre] = self._datos[padre], self._datos[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self._datos)
        while True:
            menor, izq, der = i, 2 * i + 1, 2 * i + 2
            if izq < n and self._datos[izq][:2] < self._datos[menor][:2]:
                menor = izq
            if der < n and self._datos[der][:2] < self._datos[menor][:2]:
                menor = der
            if menor == i:
                break
            self._datos[i], self._datos[menor] = self._datos[menor], self._datos[i]
            i = menor