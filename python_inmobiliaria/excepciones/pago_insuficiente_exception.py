"""Excepcion para pagos insuficientes."""

# Local application
from python_inmobiliaria.excepciones.inmobiliaria_exception import InmobiliariaException

class PagoInsuficienteException(InmobiliariaException):
    """Excepcion lanzada cuando el pago es insuficiente."""
    def __init__(self, monto_pagado: float, monto_requerido: float, numero_contrato: int):
        mensaje_usuario = f"El monto pagado es insuficiente. Se requiere ${monto_requerido:,.2f}"
        mensaje_tecnico = f"Pago insuficiente: ${monto_pagado:,.2f} < ${monto_requerido:,.2f} (Contrato {numero_contrato})"
        super().__init__(mensaje_usuario, mensaje_tecnico)
        self._monto_pagado = monto_pagado
        self._monto_requerido = monto_requerido
        self._numero_contrato = numero_contrato
    def get_monto_pagado(self) -> float:
        return self._monto_pagado
    def get_monto_requerido(self) -> float:
        return self._monto_requerido
    def get_numero_contrato(self) -> int:
        return self._numero_contrato
