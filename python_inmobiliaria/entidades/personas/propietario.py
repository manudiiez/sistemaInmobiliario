"""Entidad Propietario - Dueno de propiedades."""

# Standard library
from typing import TYPE_CHECKING, List, Optional
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class Propietario:
    """Entidad Propietario - solo contiene datos."""
    def __init__(self, dni: int, nombre: str, cbu: str, propiedades: Optional[List['Propiedad']] = None):
        self._dni = dni
        self._nombre = nombre
        self._cbu = cbu
        self._propiedades = propiedades if propiedades else []
    def get_dni(self) -> int:
        return self._dni
    def get_nombre(self) -> str:
        return self._nombre
    def get_cbu(self) -> str:
        return self._cbu
    def get_propiedades(self) -> List['Propiedad']:
        return self._propiedades.copy()
    def agregar_propiedad(self, propiedad: 'Propiedad') -> None:
        self._propiedades.append(propiedad)
