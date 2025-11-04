"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/__init__.py
# ================================================================================

"""Eventos del sistema."""


# ================================================================================
# ARCHIVO 2/3: evento_contrato.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/evento_contrato.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: evento_monitor.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/evento_monitor.py
# ================================================================================

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


