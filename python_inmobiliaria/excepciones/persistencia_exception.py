"""Excepcion para errores de persistencia."""
# Standard library
from enum import Enum
# Local application
from python_inmobiliaria.excepciones.inmobiliaria_exception import InmobiliariaException

class TipoOperacion(Enum):
    """Tipos de operaciones de persistencia."""
    LECTURA = "lectura"
    ESCRITURA = "escritura"

class PersistenciaException(InmobiliariaException):
    """Excepcion lanzada cuando falla la persistencia."""
    def __init__(self, tipo_operacion: TipoOperacion, nombre_archivo: str, causa: str):
        mensaje_usuario = f"Error en {tipo_operacion.value} del archivo {nombre_archivo}"
        mensaje_tecnico = f"Error de persistencia: {tipo_operacion.value} - {nombre_archivo} - {causa}"
        super().__init__(mensaje_usuario, mensaje_tecnico)
        self._tipo_operacion = tipo_operacion
        self._nombre_archivo = nombre_archivo
        self._causa = causa
    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion
    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo
    def get_causa(self) -> str:
        return self._causa
