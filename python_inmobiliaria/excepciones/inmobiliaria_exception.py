"""Excepcion base del sistema."""
class InmobiliariaException(Exception):
    """Excepcion base del sistema inmobiliario."""
    def __init__(self, mensaje_usuario: str, mensaje_tecnico: str):
        super().__init__(mensaje_tecnico)
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico
    def get_user_message(self) -> str:
        return self._mensaje_usuario
    def get_technical_message(self) -> str:
        return self._mensaje_tecnico
    def get_full_message(self) -> str:
        return f"{self._mensaje_usuario} | Detalle tecnico: {self._mensaje_tecnico}"
