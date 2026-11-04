# Un caso límite (vacío, no encontrado o duplicado).
# Completen el lunes 14; hoy solo el README.


import pytest

from src.cola_espera import ColaEspera
from src.indice_pacientes import IndicePacientes
from src.paciente import Paciente


def test_cola_vacia():
    cola = ColaEspera()
    with pytest.raises(ValueError, match="No hay pacientes en espera"):
        cola.desencolar()


def test_paciente_no_encontrado():
    indice = IndicePacientes()
    with pytest.raises(KeyError, match="No existe paciente"):
        indice.buscar("NO-EXISTE")


def test_paciente_duplicado():
    indice = IndicePacientes()
    indice.agregar(Paciente("P001", "Ana"))
    with pytest.raises(ValueError, match="Paciente duplicado"):
        indice.agregar(Paciente("P001", "Otra Ana"))