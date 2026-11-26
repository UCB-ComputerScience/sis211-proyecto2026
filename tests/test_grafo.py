import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from grafo_mapa import GrafoMapa
from sistema_taxis import SistemaTaxis


def mapa_de_ejemplo():
    g = GrafoMapa()
    g.agregar_calle("Plaza", "Mercado")
    g.agregar_calle("Mercado", "Hospital")
    g.agregar_calle("Hospital", "Plaza")      # ciclo: anillo de calles
    g.agregar_calle("Plaza", "Terminal")
    g.agregar_calle("Terminal", "Universidad")
    g.agregar_calle("Hospital", "Universidad")
    g.agregar_lugar("Aeropuerto")             # sin calles: no se llega
    return g


def test_ruta_directa():
    g = mapa_de_ejemplo()
    assert g.camino_mas_corto("Plaza", "Mercado") == ["Plaza", "Mercado"]


def test_ruta_con_escala_elige_la_mas_corta():
    g = mapa_de_ejemplo()
    ruta = g.camino_mas_corto("Mercado", "Universidad")
    # Hay dos caminos (por Hospital o por Plaza-Terminal):
    # el grafo devuelve el de menos tramos.
    assert ruta == ["Mercado", "Hospital", "Universidad"]


def test_hay_ciclo_y_mas_de_un_camino():
    g = mapa_de_ejemplo()
    # Plaza y Hospital se conectan directo y también vía Mercado:
    # más de un camino entre el mismo par (no es un árbol).
    assert "Hospital" in g.vecinos("Plaza")
    assert g.camino_mas_corto("Plaza", "Hospital") == ["Plaza", "Hospital"]
    assert g.se_puede_llegar("Mercado", "Plaza")


def test_caso_limite_destino_inalcanzable():
    g = mapa_de_ejemplo()
    assert g.camino_mas_corto("Plaza", "Aeropuerto") is None
    assert not g.se_puede_llegar("Plaza", "Aeropuerto")


def test_caso_limite_grafo_vacio_y_lugar_inexistente():
    g = GrafoMapa()
    assert g.camino_mas_corto("Plaza", "Terminal") is None
    g2 = mapa_de_ejemplo()
    assert g2.camino_mas_corto("Plaza", "Narnia") is None


def test_asignar_con_ruta_devuelve_la_ruta():
    s = SistemaTaxis()
    s.registrar_conductor("C1", "Ana")
    s.registrar_calle("Plaza", "Mercado")
    s.registrar_calle("Mercado", "Hospital")
    s.recibir_pedido(1, "Marta", "Plaza", "Hospital")
    pedido, conductor, ruta = s.asignar_con_ruta("C1")
    assert pedido.estado == "asignado"
    assert ruta == ["Plaza", "Mercado", "Hospital"]


def test_asignar_sin_ruta_no_rompe_ni_saca_el_pedido():
    s = SistemaTaxis()
    s.registrar_conductor("C1", "Ana")
    s.registrar_calle("Plaza", "Mercado")
    s.registrar_lugar("Aeropuerto")
    s.recibir_pedido(1, "Marta", "Plaza", "Aeropuerto")
    with pytest.raises(ValueError):
        s.asignar_con_ruta("C1")
    # el pedido sigue en la cola y el conductor sigue disponible
    assert not s.pedidos_pendientes.esta_vacia()
    assert s.buscar_conductor("C1").disponible is True
