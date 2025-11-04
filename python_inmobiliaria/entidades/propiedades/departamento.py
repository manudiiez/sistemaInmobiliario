"""Entidad Departamento - Unidad en edificio."""

# Standard library
from typing import TYPE_CHECKING, List
# Local application
from python_inmobiliaria.constantes import VALOR_BASE_DEPTO, SUPERFICIE_MINIMA_DEPTO, PISO_BASE_DEPTO, NUMERO_BASE_DEPTO
from python_inmobiliaria.entidades.propiedades.inmueble import Inmueble
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.tipo_amenidad import TipoAmenidad

class Departamento(Inmueble):
    """Entidad Departamento - solo contiene datos."""
    def __init__(self, piso: int, numero: int):
        super().__init__(valor_base=VALOR_BASE_DEPTO, superficie=SUPERFICIE_MINIMA_DEPTO)
        self._piso = piso
        self._numero = numero
        self._amenidades: List[TipoAmenidad] = []
    def get_piso(self) -> int:
        return self._piso
    def set_piso(self, piso: int) -> None:
        self._piso = piso
    def get_numero(self) -> int:
        return self._numero
    def set_numero(self, numero: int) -> None:
        self._numero = numero
    def get_amenidades(self) -> List['TipoAmenidad']:
        return self._amenidades.copy()
    def agregar_amenidad(self, amenidad: 'TipoAmenidad') -> None:
        if amenidad not in self._amenidades:
            self._amenidades.append(amenidad)
    def obtener_tipo(self) -> str:
        return "Departamento"
