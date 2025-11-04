"""Interfaz Strategy para ajuste de renta."""
# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteRentaStrategy(ABC):
    """Interfaz abstracta para estrategias de ajuste de renta."""
    @abstractmethod
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        pass
