from collections import deque
 
 
class Cola:
    """Cola FIFO: entra por el final, sale el más antiguo."""
 
    def __init__(self):
        self._datos = deque()
 
    def encolar(self, x):
        self._datos.append(x)
 
    def desencolar(self):
        if not self._datos:
            raise IndexError("La cola está vacía")
        return self._datos.popleft()
 
    def encolar_al_frente(self, x):
        """Devuelve un elemento al frente (para reponer lo que ya había salido)."""
        self._datos.appendleft(x)
 
    def esta_vacia(self):
        return len(self._datos) == 0
 
    def __len__(self):
        return len(self._datos)
 
    def __iter__(self):
        return iter(self._datos)
 
 
class Pila:
    """Pila LIFO: entra y sale por el mismo extremo."""
 
    def __init__(self):
        self._datos = []
 
    def apilar(self, x):
        self._datos.append(x)
 
    def desapilar(self):
        if not self._datos:
            raise IndexError("La pila está vacía")
        return self._datos.pop()
 
    def esta_vacia(self):
        return len(self._datos) == 0
 
    def __len__(self):
        return len(self._datos)