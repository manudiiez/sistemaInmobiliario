"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/__init__.py
# ================================================================================

"""Implementaciones de Strategy."""


# ================================================================================
# ARCHIVO 2/3: ajuste_fijo_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/ajuste_fijo_strategy.py
# ================================================================================

"""Estrategia de ajuste fijo."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteFijoStrategy(AjusteRentaStrategy):
    """Estrategia de ajuste con porcentaje fijo."""
    def __init__(self, porcentaje: float):
        self._porcentaje = porcentaje
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        return monto_actual * (1 + self._porcentaje)


# ================================================================================
# ARCHIVO 3/3: ajuste_inflacionario_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/ajuste_inflacionario_strategy.py
# ================================================================================

"""Estrategia de ajuste inflacionario."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import AJUSTE_INFLACION_ANUAL, MESES_AJUSTE_CONTRATO
from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class AjusteInflacionarioStrategy(AjusteRentaStrategy):
    """Estrategia de ajuste inflacionario anual."""
    def calcular_ajuste(self, monto_actual: float, fecha_ajuste: date, contrato: 'Contrato') -> float:
        meses_transcurridos = self._calcular_meses(contrato.get_fecha_inicio(), fecha_ajuste)
        if meses_transcurridos >= MESES_AJUSTE_CONTRATO:
            return monto_actual * AJUSTE_INFLACION_ANUAL
        else:
            return monto_actual
    def _calcular_meses(self, fecha_inicio: date, fecha_actual: date) -> int:
        delta = fecha_actual - fecha_inicio
        return delta.days // 30


