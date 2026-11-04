class ColaPrioridad:
    """Cola de prioridad implementada con min-heap.

    Menor `prioridad` = más urgente. Empate se resuelve por orden de llegada.
    """

    def __init__(self):
        self._heap = []      # entradas (prioridad, contador, paciente)
        self._contador = 0

    def encolar(self, paciente):
        self._contador += 1
        entrada = (paciente.prioridad, self._contador, paciente)
        self._heap.append(entrada)
        self._subir(len(self._heap) - 1)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("No hay pacientes en espera")
        if len(self._heap) == 1:
            _, _, paciente = self._heap.pop()
            return paciente
        _, _, paciente = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._bajar(0)
        return paciente

    def siguiente(self):
        if self.esta_vacia():
            raise ValueError("No hay pacientes en espera")
        return self._heap[0][2]

    def esta_vacia(self):
        return len(self._heap) == 0

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._heap[i] < self._heap[padre]:
                self._heap[i], self._heap[padre] = self._heap[padre], self._heap[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self._heap)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            menor = i
            if izq < n and self._heap[izq] < self._heap[menor]:
                menor = izq
            if der < n and self._heap[der] < self._heap[menor]:
                menor = der
            if menor == i:
                break
            self._heap[i], self._heap[menor] = self._heap[menor], self._heap[i]
            i = menor

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        return f"ColaPrioridad({[p for _, _, p in self._heap]!r})"