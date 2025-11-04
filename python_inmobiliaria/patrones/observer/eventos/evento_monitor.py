"""Evento de monitor."""
# Standard library
from datetime import date

class EventoMonitor:
    """Evento generico de monitor."""
    def __init__(self, fecha: date, descripcion: str):
        self._fecha = fecha
        self._descripcion = descripcion
    def get_fecha(self) -> date:
        return self._fecha
    def get_descripcion(self) -> str:
        return self._descripcion
