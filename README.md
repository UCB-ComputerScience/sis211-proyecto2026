# Sistema básico de taxis / delivery

**Autor:** Luis Fabricio Rivero Aban

**Materia:** SIS211 · Proyecto V3 (Unidad 4)

## Descripción

Sistema simple que recibe pedidos de clientes, los asigna a conductores
disponibles y permite deshacer la última asignación. En la v2, además,
puede asignar cada pedido al conductor disponible con menos viajes
completados, usando un heap. En la v3 se suma el mapa de la ciudad como
un grafo. En el flujo `asignar_con_ruta`, el sistema calcula la ruta
entre el origen y el destino del pedido y solo lo asigna si la ruta
existe.

## Estructuras de datos usadas

| Flujo del dominio | Familia | La uso porque... |
| --- | --- | --- |
| El siguiente pedido a asignar | Cola | los pedidos se atienden en el orden en que llegaron (FIFO). |
| Conductor o cliente por código | Tabla hash (`dict`) | necesito encontrarlo directo por su código, sin recorrer todo. |
| Deshacer la última asignación | Pila | la última asignación hecha es la primera que se revierte (LIFO). |
| Conductor con menos viajes | Heap (min-heap) | siempre necesito sacar al conductor con menos viajes, y el heap me da el mínimo en O(log n) sin ordenar toda la lista. |
| Ruta del viaje entre origen y destino | Grafo | las calles conectan los lugares de muchas maneras a la vez: un mismo lugar se alcanza por distintos caminos y hay ciclos (anillos de calles), así que no es una jerarquía; el grafo me deja buscar el camino más corto entre dos lugares cualesquiera con BFS. |

## Por qué el mapa es un grafo y no un árbol

El vínculo entre lugares no es un árbol: una calle conecta dos lugares
sin que uno sea «padre» del otro, un mismo par de lugares puede unirse
por más de un camino (por ejemplo, Plaza y Hospital se conectan directo
y también pasando por el Mercado) y hay ciclos, como el anillo
Plaza → Mercado → Hospital → Plaza. Una jerarquía no puede modelar eso.

**Caso límite:** un lugar puede existir en el mapa y no tener calles
todavía (en el ejemplo, el Aeropuerto). A ese destino no se llega: la
búsqueda devuelve `None` y, en el flujo de asignación, el pedido no se
asigna ni se pierde — queda en la cola y el sistema no rompe.

## Estructura del repositorio

- `src/dominio.py`: clase `Pedido`.
- `src/conductor.py`: clase `Conductor`.
- `src/estructuras.py`: implementación de `Cola` y `Pila`.
- `src/heap_conductores.py`: clase `HeapConductores` (min-heap por viajes).
- `src/grafo_mapa.py`: clase `GrafoMapa` (grafo de lugares y calles, BFS).
- `src/sistema_taxis.py`: clase `SistemaTaxis` (usa cola, dict, pila, heap y grafo).
- `src/main.py`: programa de demostración.
- `tests/test_limites.py`: pruebas de casos límite.
- `tests/test_heap.py`: pruebas del heap (vacío y orden por viajes).
- `tests/test_grafo.py`: pruebas del grafo (ruta más corta, ciclo y destino inalcanzable).

## Cómo ejecutarlo

Requisitos: Python 3.10 o superior (sin librerías externas).

```bash
git clone https://github.com/luisriveroa/sis211-proyecto2026.git
cd sis211-proyecto2026
python src/main.py
```

## Pruebas

```bash
pip install pytest
python -m pytest tests
```

## Ejemplo de uso

1. Se registran conductores y se crean pedidos.
2. Se asigna el siguiente pedido de la cola a un conductor disponible.
3. Se busca un conductor por código.
4. Se deshace la última asignación (el pedido vuelve al frente de la cola).
5. Se asigna el siguiente pedido al conductor con menos viajes (heap).
6. Si no hay conductores disponibles, el sistema no rompe y el pedido sigue en la cola.
7. Se registran las calles de la ciudad y se calcula la ruta del viaje (grafo): Plaza 25 de Mayo → Terminal → Universidad.
8. Si el destino no tiene calles (Aeropuerto), no hay ruta: el pedido no se asigna y sigue en la cola.
