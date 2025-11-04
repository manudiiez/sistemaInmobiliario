"""Evento de contrato."""
# Standard library
from datetime import date

class EventoContrato:
    """Evento relacionado con contratos."""
    def __init__(self, numero_contrato: int, tipo_evento: str, fecha: date):
        self._numero_contrato = numero_contrato
        self._tipo_evento = tipo_evento
        self._fecha = fecha
    def get_numero_contrato(self) -> int:
        return self._numero_contrato
    def get_tipo_evento(self) -> str:
        return self._tipo_evento
    def get_fecha(self) -> date:
        return self._fecha
