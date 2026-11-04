import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from sistema_taxis import SistemaTaxis


def test_heap_vacio_no_rompe():
    sistema = SistemaTaxis()
    sistema.recibir_pedido(1, "Ana", "A", "B")
    assert sistema.asignar_al_menos_cargado() is None
    assert not sistema.pedidos_pendientes.esta_vacia()


def test_elige_el_de_menos_viajes():
    sistema = SistemaTaxis()
    sistema.registrar_conductor("C1", "Luis")
    sistema.registrar_conductor("C2", "Marta")
    sistema.recibir_pedido(1, "Ana", "A", "B")
    sistema.recibir_pedido(2, "Beto", "C", "D")
    sistema.recibir_pedido(3, "Eva", "E", "F")

    _, conductor = sistema.asignar_al_menos_cargado()
    assert conductor.codigo == "C1"
    sistema.completar_viaje("C1")
    _, conductor = sistema.asignar_al_menos_cargado()
    assert conductor.codigo == "C2"


def test_asignar_manualmente_y_completar_actualiza_prioridad():
    sistema = SistemaTaxis()
    sistema.registrar_conductor("C1", "Luis")
    sistema.registrar_conductor("C2", "Marta")
    sistema.recibir_pedido(1, "Ana", "A", "B")
    sistema.recibir_pedido(2, "Beto", "C", "D")

    sistema.asignar_siguiente("C1")
    sistema.completar_viaje("C1")
    _, conductor = sistema.asignar_al_menos_cargado()
    assert conductor.codigo == "C2"
