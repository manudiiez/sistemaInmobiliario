"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/__init__.py
# ================================================================================

"""Excepciones personalizadas del sistema."""


# ================================================================================
# ARCHIVO 2/6: contrato_vencido_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/contrato_vencido_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: inmobiliaria_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/inmobiliaria_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/mensajes_exception.py
# ================================================================================

"""Mensajes centralizados de excepciones."""
MENSAJE_CONTRATO_VENCIDO = "El contrato se encuentra vencido"
MENSAJE_PAGO_INSUFICIENTE = "El monto pagado es insuficiente"
MENSAJE_PERSISTENCIA_ERROR = "Error en operacion de persistencia"
MENSAJE_PROPIETARIO_INVALIDO = "El nombre del propietario no puede ser nulo o vacio"


# ================================================================================
# ARCHIVO 5/6: pago_insuficiente_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/pago_insuficiente_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: persistencia_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/persistencia_exception.py
# ================================================================================

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


