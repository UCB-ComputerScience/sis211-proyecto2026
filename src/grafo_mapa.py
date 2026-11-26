from collections import deque


class GrafoMapa:
    """Grafo no dirigido de lugares conectados por calles.

    Cada lugar es un nodo y cada calle una arista en ambos sentidos.
    No es un árbol: un lugar puede tener varios vecinos, hay ciclos
    (anillos de calles) y puede haber lugares sin calles todavía.
    """

    def __init__(self):
        self._vecinos = {}  # lugar -> conjunto de lugares vecinos

    def agregar_lugar(self, lugar):
        if lugar not in self._vecinos:
            self._vecinos[lugar] = set()

    def agregar_calle(self, a, b):
        """Conecta dos lugares en ambos sentidos; los crea si no existen."""
        self.agregar_lugar(a)
        self.agregar_lugar(b)
        self._vecinos[a].add(b)
        self._vecinos[b].add(a)

    def vecinos(self, lugar):
        return set(self._vecinos.get(lugar, set()))

    def camino_mas_corto(self, origen, destino):
        """BFS: devuelve la ruta con menos tramos, como lista de lugares.

        Devuelve None si el destino no existe o no se puede llegar
        (caso límite: un lugar sin calles queda aislado del resto).
        """
        if origen not in self._vecinos or destino not in self._vecinos:
            return None
        if origen == destino:
            return [origen]

        visitados = {origen}
        padre = {}
        cola = deque([origen])
        while cola:
            actual = cola.popleft()
            for vecino in self._vecinos[actual]:
                if vecino in visitados:
                    continue
                visitados.add(vecino)
                padre[vecino] = actual
                if vecino == destino:
                    ruta = [destino]
                    while ruta[-1] != origen:
                        ruta.append(padre[ruta[-1]])
                    ruta.reverse()
                    return ruta
                cola.append(vecino)
        return None

    def se_puede_llegar(self, origen, destino):
        return self.camino_mas_corto(origen, destino) is not None
