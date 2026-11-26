from estructuras import Cola, Pila
from dominio import Pedido
from conductor import Conductor
from heap_conductores import HeapConductores
from grafo_mapa import GrafoMapa

class SistemaTaxis:
    """
    Tres familias, cada una en un flujo real:
      - Cola (FIFO): pedidos pendientes, se asigna el más antiguo.
      - Tabla hash (dict): conductores por código, búsqueda directa.
      - Pila (LIFO): asignaciones hechas, se deshace la más reciente.
    """

    def __init__(self):
        self.pedidos_pendientes = Cola()
        self.conductores = {}            # código -> Conductor
        self.asignaciones = Pila()       # (pedido, conductor)
        self.heap_conductores = HeapConductores()
        self.mapa = GrafoMapa()          # lugares y calles de la ciudad

    # --- conductores (tabla hash) ---
    def registrar_conductor(self, codigo, nombre):
        if codigo in self.conductores:
            raise ValueError(f"Ya existe el conductor {codigo}")
        self.conductores[codigo] = Conductor(codigo, nombre)
        self.heap_conductores.insertar(self.conductores[codigo])

    def buscar_conductor(self, codigo):
        return self.conductores.get(codigo)

    # --- pedidos (cola) ---
    def recibir_pedido(self, id_pedido, cliente, origen, destino):
        pedido = Pedido(id_pedido, cliente, origen, destino)
        self.pedidos_pendientes.encolar(pedido)
        return pedido

    def asignar_siguiente(self, codigo_conductor):
        conductor = self.buscar_conductor(codigo_conductor)
        if conductor is None:
            raise KeyError(f"No existe el conductor {codigo_conductor}")
        if not conductor.disponible:
            raise ValueError(f"El conductor {codigo_conductor} está ocupado")
        if self.pedidos_pendientes.esta_vacia():
            raise IndexError("No hay pedidos pendientes")

        pedido = self.pedidos_pendientes.desencolar()
        pedido.estado = "asignado"
        conductor.disponible = False
        self.heap_conductores.eliminar(conductor)
        self.asignaciones.apilar((pedido, conductor))
        return pedido, conductor

    # --- deshacer (pila) ---
    def deshacer_ultima_asignacion(self):
        if self.asignaciones.esta_vacia():
            raise IndexError("No hay asignaciones para deshacer")
        pedido, conductor = self.asignaciones.desapilar()
        pedido.estado = "pendiente"
        conductor.disponible = True
        # era el más antiguo cuando se asignó: vuelve al frente de la cola
        self.pedidos_pendientes.encolar_al_frente(pedido)
        self.heap_conductores.insertar(conductor)
        return pedido, conductor

    # --- v2: conductor con menos viajes (heap) ---
    def asignar_al_menos_cargado(self):
        if self.pedidos_pendientes.esta_vacia():
            raise IndexError("No hay pedidos pendientes")

        while True:
            conductor = self.heap_conductores.extraer()
            if conductor is None:
                return None
            if conductor.disponible:
                break

        pedido = self.pedidos_pendientes.desencolar()
        pedido.estado = "asignado"
        conductor.disponible = False
        self.asignaciones.apilar((pedido, conductor))
        return pedido, conductor

    def completar_viaje(self, codigo_conductor):
        conductor = self.buscar_conductor(codigo_conductor)
        if conductor is None:
            raise KeyError(f"No existe el conductor {codigo_conductor}")
        if conductor.disponible:
            raise ValueError(f"El conductor {codigo_conductor} no tiene viaje")
        conductor.disponible = True
        conductor.viajes += 1
        self.heap_conductores.insertar(conductor)

    # --- v3: rutas del viaje con el grafo del mapa ---
    def registrar_lugar(self, lugar):
        self.mapa.agregar_lugar(lugar)

    def registrar_calle(self, a, b):
        self.mapa.agregar_calle(a, b)

    def calcular_ruta(self, origen, destino):
        """Ruta con menos tramos entre origen y destino; None si no se llega."""
        return self.mapa.camino_mas_corto(origen, destino)

    def asignar_con_ruta(self, codigo_conductor):
        """Asigna el siguiente pedido solo si existe ruta para su viaje.

        Si el destino no se alcanza en el mapa (caso límite), el pedido
        no se asigna y queda en la cola: el sistema no rompe.
        """
        conductor = self.buscar_conductor(codigo_conductor)
        if conductor is None:
            raise KeyError(f"No existe el conductor {codigo_conductor}")
        if not conductor.disponible:
            raise ValueError(f"El conductor {codigo_conductor} está ocupado")
        if self.pedidos_pendientes.esta_vacia():
            raise IndexError("No hay pedidos pendientes")

        siguiente = next(iter(self.pedidos_pendientes))
        ruta = self.mapa.camino_mas_corto(siguiente.origen, siguiente.destino)
        if ruta is None:
            raise ValueError(
                f"Sin ruta de {siguiente.origen} a {siguiente.destino}: "
                "el pedido sigue en la cola"
            )
        pedido, conductor = self.asignar_siguiente(codigo_conductor)
        return pedido, conductor, ruta
