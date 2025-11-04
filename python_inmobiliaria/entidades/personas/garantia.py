"""Entidad Garantia - Garantia de alquiler."""
# Standard library
from datetime import date

class Garantia:
    """Entidad Garantia - solo contiene datos."""
    def __init__(self, tipo: str, monto: float, fecha_constitucion: date):
        self._tipo = tipo
        self._monto = monto
        self._fecha_constitucion = fecha_constitucion
        self._activa = True
    def get_tipo(self) -> str:
        return self._tipo
    def get_monto(self) -> float:
        return self._monto
    def get_fecha_constitucion(self) -> date:
        return self._fecha_constitucion
    def esta_activa(self) -> bool:
        return self._activa
    def desactivar(self) -> None:
        self._activa = False
