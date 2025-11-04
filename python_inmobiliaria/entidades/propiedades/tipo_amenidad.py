"""Enumeracion de tipos de amenidades."""
# Standard library
from enum import Enum

class TipoAmenidad(Enum):
    """Tipos de amenidades disponibles en departamentos."""
    PISCINA = "Piscina"
    GIMNASIO = "Gimnasio"
    SEGURIDAD = "Seguridad"
    SALON_EVENTOS = "Salon de Eventos"
