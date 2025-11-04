"""
Clase base para inmuebles edificados.

Este modulo define la clase base para propiedades que son construcciones
como casas y departamentos.
"""

# Local application
from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad


class Inmueble(Propiedad):
    """Clase base para inmuebles edificados (Casa, Departamento)."""

    def __init__(self, valor_base: float, superficie: float):
        """
        Inicializa un inmueble.

        Args:
            valor_base: Valor base del inmueble
            superficie: Superficie en metros cuadrados
        """
        super().__init__(valor_base, superficie)

    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de inmueble.

        Returns:
            Tipo generico Inmueble
        """
        return "Inmueble"
