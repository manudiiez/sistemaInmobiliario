"""Estrategia de ajuste inflacionario."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import AJUSTE_INFLACION_ANUAL, MESES_AJUSTE_CONTRATO
from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteInflacionarioStrategy(AjusteRentaStrategy):
    """Estrategia de ajuste inflacionario anual."""
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        meses_transcurridos = self._calcular_meses(contrato.get_fecha_inicio(), fecha_ajuste)
        if meses_transcurridos >= MESES_AJUSTE_CONTRATO:
            return monto_actual * AJUSTE_INFLACION_ANUAL
        else:
            return monto_actual
    def _calcular_meses(self, fecha_inicio: date, fecha_actual: date) -> int:
        delta = fecha_actual - fecha_inicio
        return delta.days // 30
