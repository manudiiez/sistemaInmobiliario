"""Estrategia de ajuste fijo."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteFijoStrategy(AjusteRentaStrategy):
    """Estrategia de ajuste con porcentaje fijo."""
    def __init__(self, porcentaje: float):
        self._porcentaje = porcentaje
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        return monto_actual * (1 + self._porcentaje)
