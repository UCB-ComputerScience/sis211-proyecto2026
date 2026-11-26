# Clase del dominio: un pedido de taxi/delivery.
# Las estructuras (cola, pila, hash) viven en estructuras.py y sistema_taxis.py.


class Pedido:
    def __init__(self, codigo, cliente, origen, destino):
        self.codigo = codigo
        self.cliente = cliente
        self.origen = origen
        self.destino = destino
        self.estado = "pendiente"  # pendiente | asignado

    def __repr__(self):
        return f"Pedido({self.codigo}, {self.cliente}, {self.origen} -> {self.destino}, {self.estado})"