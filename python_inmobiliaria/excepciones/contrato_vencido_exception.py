"""Excepcion para contratos vencidos."""
# Standard library
from datetime import date
# Local application
from python_inmobiliaria.excepciones.inmobiliaria_exception import InmobiliariaException

class ContratoVencidoException(InmobiliariaException):
    """Excepcion lanzada cuando un contrato esta vencido."""
    def __init__(self, fecha_vencimiento: date, fecha_actual: date):
        mensaje_usuario = "El contrato se encuentra vencido"
        mensaje_tecnico = f"Contrato vencido el {fecha_vencimiento}, fecha actual {fecha_actual}"
        super().__init__(mensaje_usuario, mensaje_tecnico)
        self._fecha_vencimiento = fecha_vencimiento
        self._fecha_actual = fecha_actual
    def get_fecha_vencimiento(self) -> date:
        return self._fecha_vencimiento
    def get_fecha_actual(self) -> date:
        return self._fecha_actual
