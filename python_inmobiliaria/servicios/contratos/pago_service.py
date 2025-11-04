"""Servicio para pagos."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.entidades.contratos.pago import Pago
from python_inmobiliaria.excepciones.pago_insuficiente_exception import PagoInsuficienteException
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class PagoService:
    """Servicio para pagos."""
    def registrar_pago(self, contrato: 'Contrato', monto: float, fecha_pago: date) -> Pago:
        monto_requerido = contrato.get_monto_mensual()
        if monto < monto_requerido:
            raise PagoInsuficienteException(monto_pagado=monto, monto_requerido=monto_requerido, numero_contrato=contrato.get_numero_contrato())
        pago = Pago(monto=monto, fecha_pago=fecha_pago, numero_contrato=contrato.get_numero_contrato())
        return pago
