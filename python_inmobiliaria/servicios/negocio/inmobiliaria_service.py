"""Servicio de alto nivel para inmobiliaria."""
# Standard library
from typing import Dict, Optional, TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

class InmobiliariaService:
    """Servicio de alto nivel para operaciones inmobiliarias."""
    def __init__(self):
        self._propiedades: Dict[str, 'RegistroInmobiliario'] = {}
    def add_propiedad(self, registro: 'RegistroInmobiliario') -> None:
        direccion = registro.get_propiedad().get_direccion()
        self._propiedades[direccion] = registro
    def buscar_propiedad(self, direccion: str) -> Optional['RegistroInmobiliario']:
        return self._propiedades.get(direccion)
