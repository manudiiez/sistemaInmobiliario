"""Entidad Pago - Registro de pago de alquiler."""
# Standard library
from datetime import date

class Pago:
    """Entidad Pago - solo contiene datos."""
    def __init__(self, monto: float, fecha_pago: date, numero_contrato: int):
        self._monto = monto
        self._fecha_pago = fecha_pago
        self._numero_contrato = numero_contrato
    def get_monto(self) -> float:
        return self._monto
    def get_fecha_pago(self) -> date:
        return self._fecha_pago
    def get_numero_contrato(self) -> int:
        return self._numero_contrato

