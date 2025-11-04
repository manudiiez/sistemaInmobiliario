"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/__init__.py
# ================================================================================

"""Entidades relacionadas con contratos."""


# ================================================================================
# ARCHIVO 2/3: contrato.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/contrato.py
# ================================================================================

"""Entidad Contrato - Contrato de arrendamiento."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.personas.inquilino import Inquilino
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad


class Contrato:
    """Entidad Contrato - solo contiene datos."""
    def __init__(self, numero_contrato: int, fecha_inicio: date, fecha_vencimiento: date, monto_mensual: float, inquilino: 'Inquilino', propiedad: 'Propiedad'):
        if monto_mensual < 0:
            raise ValueError("El monto mensual no puede ser negativo")
        self._numero_contrato = numero_contrato
        self._fecha_inicio = fecha_inicio
        self._fecha_vencimiento = fecha_vencimiento
        self._monto_mensual = monto_mensual
        self._inquilino = inquilino
        self._propiedad = propiedad
    def get_numero_contrato(self) -> int:
        return self._numero_contrato
    def get_fecha_inicio(self) -> date:
        return self._fecha_inicio
    def set_fecha_inicio(self, fecha_inicio: date) -> None:
        self._fecha_inicio = fecha_inicio
    def get_fecha_vencimiento(self) -> date:
        return self._fecha_vencimiento
    def set_fecha_vencimiento(self, fecha_vencimiento: date) -> None:
        self._fecha_vencimiento = fecha_vencimiento
    def get_monto_mensual(self) -> float:
        return self._monto_mensual
    def set_monto_mensual(self, monto_mensual: float) -> None:
        if monto_mensual < 0:
            raise ValueError("El monto mensual no puede ser negativo")
        self._monto_mensual = monto_mensual
    def get_inquilino(self) -> 'Inquilino':
        return self._inquilino
    def get_propiedad(self) -> 'Propiedad':
        return self._propiedad


# ================================================================================
# ARCHIVO 3/3: pago.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/pago.py
# ================================================================================

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



