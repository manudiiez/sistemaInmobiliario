"""Servicio para contratos."""
# Standard library
from datetime import date, timedelta
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import MESES_AJUSTE_CONTRATO
from python_inmobiliaria.excepciones.contrato_vencido_exception import ContratoVencidoException
from python_inmobiliaria.patrones.strategy.impl.ajuste_inflacionario_strategy import AjusteInflacionarioStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy

class ContratoService:
    """Servicio para contratos con Strategy Pattern."""
    def __init__(self):
        self._estrategia_ajuste: 'AjusteRentaStrategy' = AjusteInflacionarioStrategy()
    def aplicar_ajuste(self, contrato: 'Contrato') -> float:
        if date.today() > contrato.get_fecha_vencimiento():
            raise ContratoVencidoException(contrato.get_fecha_vencimiento(), date.today())
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato.get_monto_mensual(), date.today(), contrato)
        contrato.set_monto_mensual(nuevo_monto)
        return nuevo_monto
    def renovar_contrato(self, contrato_anterior: 'Contrato', duracion_meses: int) -> 'Contrato':
        from python_inmobiliaria.entidades.contratos.contrato import Contrato
        fecha_inicio_nueva = date.today()
        fecha_vencimiento_nueva = fecha_inicio_nueva + timedelta(days=duracion_meses * 30)
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato_anterior.get_monto_mensual(), fecha_inicio_nueva, contrato_anterior)
        nuevo_contrato = Contrato(numero_contrato=contrato_anterior.get_numero_contrato() + 1, fecha_inicio=fecha_inicio_nueva, fecha_vencimiento=fecha_vencimiento_nueva, monto_mensual=nuevo_monto, inquilino=contrato_anterior.get_inquilino(), propiedad=contrato_anterior.get_propiedad())
        return nuevo_contrato
