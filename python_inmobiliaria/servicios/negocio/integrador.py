"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/__init__.py
# ================================================================================

"""Servicios de alto nivel."""


# ================================================================================
# ARCHIVO 2/3: inmobiliaria_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/inmobiliaria_service.py
# ================================================================================

"""Servicio de alto nivel para inmobiliaria."""
# Standard library
from typing import Dict, Optional, TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

class InmobiliariaService:
    """Servicio de alto nivel para operaciones inmobiliarias."""
    def __init__(self):
        self._propiedades: Dict[str, 'RegistroInmobiliario'] = {}
    def add_propiedad(self, registro: 'RegistroInmobiliario') -> None:
        direccion = registro.get_propiedad().get_direccion()
        self._propiedades[direccion] = registro
    def buscar_propiedad(self, direccion: str) -> Optional['RegistroInmobiliario']:
        return self._propiedades.get(direccion)


# ================================================================================
# ARCHIVO 3/3: reporte.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/reporte.py
# ================================================================================

"""Servicio de reportes."""
class Reporte:
    """Servicio para generacion de reportes."""
    def generar_reporte_simple(self, titulo: str, contenido: str) -> None:
        print()
        print("=" * 70)
        print(f"  {titulo}")
        print("=" * 70)
        print(contenido)
        print("=" * 70)


