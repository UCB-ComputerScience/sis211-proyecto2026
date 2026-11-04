import pytest

from src.cola_prioridad import ColaPrioridad
from src.paciente import Paciente


def test_cola_prioridad_vacia():
    cola = ColaPrioridad()
    with pytest.raises(ValueError, match="No hay pacientes en espera"):
        cola.desencolar()


def test_atender_al_mas_critico_primero():
    cola = ColaPrioridad()
    cola.encolar(Paciente("P001", "Ana", prioridad=3))
    cola.encolar(Paciente("P002", "Luis", prioridad=1))   # crítico
    cola.encolar(Paciente("P003", "Eva", prioridad=5))

    primero = cola.desencolar()
    assert primero.codigo == "P002"
    assert primero.prioridad == 1


def test_empate_respeta_orden_de_llegada():
    cola = ColaPrioridad()
    cola.encolar(Paciente("A", "A", prioridad=2))
    cola.encolar(Paciente("B", "B", prioridad=2))

    assert cola.desencolar().codigo == "A"
    assert cola.desencolar().codigo == "B"