# SIS-211 · Proyecto de curso (2/2026)

Un mismo software que **crece**: v1 (estructuras simples) → v2 (jerárquicas) → v3 (grafos).

**Hoy solo existe la branch `v1`.** No creen `v2` ni `v3`.

| | |
| --- | --- |
| **Estudiante** | Alejandro Cruz |
| **Dominio** | Sistema de atención de pacientes |
| **Repo** | [https://github.com/al3-cruz/sis211-proyecto2026](https://github.com/al3-cruz/sis211-proyecto2026/tree/v2) |

## Mapa v1 (mínimo tres familias distintas)

Familias: arreglo, lista, pila, cola, tabla hash.  
`dict` y `set` son **la misma** familia (hash). Sin árboles ni grafos en v1.

| Flujo del dominio | Qué llega / sale / se busca | Familia | La uso porque… |
| --- | --- | --- | --- |
| El siguiente paciente a atender | Sale el primero que llegó; se respeta orden de llegada | cola | La sala de espera atiende por orden FIFO. |
| Buscar un paciente por código o CI | Se busca por código/CI y se obtiene su ficha | tabla hash | Acceso rápido O(1) por clave única. |
| Historial de atenciones de un paciente | Se guardan y recorren atenciones en orden cronológico | lista | Mantiene el orden de los eventos y permite recorrerlos. |

Cómo probar un caso límite (vacío, no encontrado o duplicado):

> Caso vacío: si la cola de espera está vacía y se pide el siguiente paciente, `ColaEspera.desencolar()` lanza `ValueError`.  
> No encontrado: si se busca un código inexistente en `IndicePacientes.buscar()`, lanza `KeyError`.  
> Duplicado: si se registra un paciente con código ya existente, `IndicePacientes.agregar()` lanza `ValueError`.

## Carpetas

- `src/` — clases del dominio (POO). Hoy no codeen.
- `tests/` — un caso límite, cuando implementen.

## Alcance

- v1: clases en `.py` (POO). Entrega Moodle: **2026-10-07 23:59**.
- Este README **no** sustituye la tarea de Moodle.
- v2 y v3: otras branches, más adelante, a partir de `v1`.


## v2 — Jerarquía (heap de prioridad)

Branch: `v2` (desde `v1`). No se reescribe v1: se suma una jerarquía usada en un flujo.

| Flujo del dominio | Qué llega / sale / se busca | Familia | La uso porque… |
| --- | --- | --- | --- |
| El siguiente paciente a atender por gravedad | Sale el paciente más urgente (menor número de prioridad) | heap (min-heap) | La sala de urgencias atiende primero a los críticos, no por orden de llegada. |

**Clase nueva:** `ColaPrioridad` en `src/cola_prioridad.py`.  
**Prioridades:** 1 = crítico, 2 = grave, 3 = normal, 4 = leve, 5 = mínimo.  
**Empate:** se respeta el orden de llegada mediante un contador interno.

Cómo probar un caso límite v2:

> Si la `ColaPrioridad` está vacía y se llama `desencolar()`, lanza `ValueError`. Si se encolan prioridades 3, 1 y 5, el primero en salir es el 1. Si dos pacientes tienen la misma prioridad, sale primero el que llegó antes.
