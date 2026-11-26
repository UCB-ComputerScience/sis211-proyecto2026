import os
import sys

import pytest

# src/ usa imports simples (from estructuras import ...), así que se agrega al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from sistema_taxis import SistemaTaxis


def test_asignar_con_cola_vacia():
    sistema = SistemaTaxis()
    sistema.registrar_conductor("C1", "Ana")
    with pytest.raises(IndexError):
        sistema.asignar_siguiente("C1")


def test_buscar_conductor_inexistente():
    sistema = SistemaTaxis()
    assert sistema.buscar_conductor("X9") is None


def test_conductor_duplicado():
    sistema = SistemaTaxis()
    sistema.registrar_conductor("C1", "Ana")
    with pytest.raises(ValueError):
        sistema.registrar_conductor("C1", "Otro")


def test_deshacer_sin_asignaciones():
    sistema = SistemaTaxis()
    with pytest.raises(IndexError):
        sistema.deshacer_ultima_asignacion()


def test_deshacer_devuelve_pedido_al_frente():
    sistema = SistemaTaxis()
    sistema.registrar_conductor("C1", "Ana")
    sistema.recibir_pedido(1, "Marta", "Plaza", "Terminal")
    sistema.recibir_pedido(2, "Jorge", "Mercado", "Hospital")
    pedido, conductor = sistema.asignar_siguiente("C1")
    sistema.deshacer_ultima_asignacion()
    assert conductor.disponible is True
    assert list(sistema.pedidos_pendientes)[0] is pedido
