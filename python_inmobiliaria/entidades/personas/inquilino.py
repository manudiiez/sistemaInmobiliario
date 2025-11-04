"""Entidad Inquilino - Persona arrendataria."""
# Standard library
from typing import TYPE_CHECKING, List, Optional

# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.personas.garantia import Garantia
    from python_inmobiliaria.entidades.personas.referencia import Referencia

class Inquilino:
    """Entidad Inquilino - solo contiene datos."""
    def __init__(self, dni: int, nombre: str, telefono: str, referencias: Optional[List['Referencia']] = None):
        self._dni = dni
        self._nombre = nombre
        self._telefono = telefono
        self._referencias = referencias if referencias else []
        self._garantia: Optional['Garantia'] = None
    def get_dni(self) -> int:
        return self._dni
    def get_nombre(self) -> str:
        return self._nombre
    def get_telefono(self) -> str:
        return self._telefono
    def get_referencias(self) -> List['Referencia']:
        return self._referencias.copy()
    def agregar_referencia(self, referencia: 'Referencia') -> None:
        self._referencias.append(referencia)
    def get_garantia(self) -> Optional['Garantia']:
        return self._garantia
    def set_garantia(self, garantia: 'Garantia') -> None:
        self._garantia = garantia
