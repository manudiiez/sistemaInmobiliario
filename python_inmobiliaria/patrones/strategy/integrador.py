"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/__init__.py
# ================================================================================

"""Patron Strategy."""


# ================================================================================
# ARCHIVO 2/2: ajuste_renta_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/ajuste_renta_strategy.py
# ================================================================================

"""Interfaz Strategy para ajuste de renta."""
# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteRentaStrategy(ABC):
    """Interfaz abstracta para estrategias de ajuste de renta."""
    @abstractmethod
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        pass


