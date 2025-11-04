"""
Entidad Casa - Propiedad unifamiliar.

Este modulo define la entidad Casa con sus caracteristicas especificas
como terreno, plantas y garaje.
"""

# Local application
from python_inmobiliaria.constantes import (
    VALOR_BASE_CASA,
    SUPERFICIE_MINIMA_CASA,
    TERRENO_BASE_CASA,
    PLANTAS_BASE_CASA
)
from python_inmobiliaria.entidades.propiedades.inmueble import Inmueble


class Casa(Inmueble):
    """Entidad Casa - solo contiene datos."""

    def __init__(self, terreno: float, plantas: int, garaje: bool):
        """
        Inicializa una casa.

        Args:
            terreno: Metros cuadrados de terreno
            plantas: Cantidad de plantas
            garaje: Indica si tiene garaje
        """
        super().__init__(
            valor_base=VALOR_BASE_CASA,
            superficie=SUPERFICIE_MINIMA_CASA
        )
        self._terreno = terreno
        self._plantas = plantas
        self._garaje = garaje

    def get_terreno(self) -> float:
        """Retorna los metros de terreno."""
        return self._terreno

    def set_terreno(self, terreno: float) -> None:
        """Establece los metros de terreno."""
        self._terreno = terreno

    def get_plantas(self) -> int:
        """Retorna la cantidad de plantas."""
        return self._plantas

    def set_plantas(self, plantas: int) -> None:
        """Establece la cantidad de plantas."""
        self._plantas = plantas

    def tiene_garaje(self) -> bool:
        """Retorna si tiene garaje."""
        return self._garaje

    def set_garaje(self, garaje: bool) -> None:
        """Establece si tiene garaje."""
        self._garaje = garaje

    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de propiedad.

        Returns:
            Tipo Casa
        """
        return "Casa"
