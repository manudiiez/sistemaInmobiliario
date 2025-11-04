"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/registros
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/registros/__init__.py
# ================================================================================

"""Entidades de registros inmobiliarios."""


# ================================================================================
# ARCHIVO 2/2: registro_inmobiliario.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/registros/registro_inmobiliario.py
# ================================================================================

"""Entidad RegistroInmobiliario - Registro completo de propiedad."""
# Standard library
from typing import TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class RegistroInmobiliario:
    """Entidad RegistroInmobiliario - solo contiene datos."""
    def __init__(self, id_registro: int, propiedad: 'Propiedad', contrato: 'Contrato', propietario: str, valor_fiscal: float):
        self._id_registro = id_registro
        self._propiedad = propiedad
        self._contrato = contrato
        self._propietario = propietario
        self._valor_fiscal = valor_fiscal
    def get_id_registro(self) -> int:
        return self._id_registro
    def get_propiedad(self) -> 'Propiedad':
        return self._propiedad
    def get_contrato(self) -> 'Contrato':
        return self._contrato
    def get_propietario(self) -> str:
        return self._propietario
    def get_valor_fiscal(self) -> float:
        return self._valor_fiscal


