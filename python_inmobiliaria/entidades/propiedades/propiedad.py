"""
Interfaz base para todas las propiedades inmobiliarias.

Este modulo define la interfaz abstracta que todas las propiedades
deben implementar.
"""
# Standard library
from abc import ABC, abstractmethod


class Propiedad(ABC):
    """Interfaz base abstracta para propiedades inmobiliarias."""

    def __init__(self, valor_base: float, superficie: float):
        """
        Inicializa una propiedad.

        Args:
            valor_base: Valor base de la propiedad
            superficie: Superficie en metros cuadrados

        Raises:
            ValueError: Si superficie es menor o igual a cero
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        
        self._valor_base = valor_base
        self._superficie = superficie
        self._direccion = ""
        self._propietario_dni = 0

    def get_valor_base(self) -> float:
        """Retorna el valor base de la propiedad."""
        return self._valor_base

    def set_valor_base(self, valor_base: float) -> None:
        """Establece el valor base de la propiedad."""
        self._valor_base = valor_base

    def get_superficie(self) -> float:
        """Retorna la superficie de la propiedad."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie de la propiedad.

        Args:
            superficie: Superficie en metros cuadrados

        Raises:
            ValueError: Si superficie es menor o igual a cero
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_direccion(self) -> str:
        """Retorna la direccion de la propiedad."""
        return self._direccion

    def set_direccion(self, direccion: str) -> None:
        """Establece la direccion de la propiedad."""
        self._direccion = direccion

    def get_propietario_dni(self) -> int:
        """Retorna el DNI del propietario."""
        return self._propietario_dni

    def set_propietario_dni(self, propietario_dni: int) -> None:
        """Establece el DNI del propietario."""
        self._propietario_dni = propietario_dni

    @abstractmethod
    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de propiedad.

        Returns:
            Tipo de propiedad como string
        """
        pass
