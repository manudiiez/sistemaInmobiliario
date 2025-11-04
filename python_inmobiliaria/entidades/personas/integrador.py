"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/__init__.py
# ================================================================================

"""Entidades relacionadas con personas."""


# ================================================================================
# ARCHIVO 2/5: garantia.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/garantia.py
# ================================================================================

"""Entidad Garantia - Garantia de alquiler."""
# Standard library
from datetime import date

class Garantia:
    """Entidad Garantia - solo contiene datos."""
    def __init__(self, tipo: str, monto: float, fecha_constitucion: date):
        self._tipo = tipo
        self._monto = monto
        self._fecha_constitucion = fecha_constitucion
        self._activa = True
    def get_tipo(self) -> str:
        return self._tipo
    def get_monto(self) -> float:
        return self._monto
    def get_fecha_constitucion(self) -> date:
        return self._fecha_constitucion
    def esta_activa(self) -> bool:
        return self._activa
    def desactivar(self) -> None:
        self._activa = False


# ================================================================================
# ARCHIVO 3/5: inquilino.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/inquilino.py
# ================================================================================

"""Entidad Inquilino - Persona arrendataria."""
# Standard library
from typing import TYPE_CHECKING, List, Optional

# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.personas.garantia import Garantia
    from python_inmobiliaria.entidades.personas.referencia import Referencia

class Inquilino:
    """Entidad Inquilino - solo contiene datos."""
    def __init__(self, dni: int, nombre: str, telefono: str, referencias: Optional[List['Referencia']] = None):
        self._dni = dni
        self._nombre = nombre
        self._telefono = telefono
        self._referencias = referencias if referencias else []
        self._garantia: Optional['Garantia'] = None
    def get_dni(self) -> int:
        return self._dni
    def get_nombre(self) -> str:
        return self._nombre
    def get_telefono(self) -> str:
        return self._telefono
    def get_referencias(self) -> List['Referencia']:
        return self._referencias.copy()
    def agregar_referencia(self, referencia: 'Referencia') -> None:
        self._referencias.append(referencia)
    def get_garantia(self) -> Optional['Garantia']:
        return self._garantia
    def set_garantia(self, garantia: 'Garantia') -> None:
        self._garantia = garantia


# ================================================================================
# ARCHIVO 4/5: propietario.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/propietario.py
# ================================================================================

"""Entidad Propietario - Dueno de propiedades."""

# Standard library
from typing import TYPE_CHECKING, List, Optional
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class Propietario:
    """Entidad Propietario - solo contiene datos."""
    def __init__(self, dni: int, nombre: str, cbu: str, propiedades: Optional[List['Propiedad']] = None):
        self._dni = dni
        self._nombre = nombre
        self._cbu = cbu
        self._propiedades = propiedades if propiedades else []
    def get_dni(self) -> int:
        return self._dni
    def get_nombre(self) -> str:
        return self._nombre
    def get_cbu(self) -> str:
        return self._cbu
    def get_propiedades(self) -> List['Propiedad']:
        return self._propiedades.copy()
    def agregar_propiedad(self, propiedad: 'Propiedad') -> None:
        self._propiedades.append(propiedad)


# ================================================================================
# ARCHIVO 5/5: referencia.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/referencia.py
# ================================================================================

"""Entidad Referencia - Referencia personal."""
class Referencia:
    """Entidad Referencia - solo contiene datos."""
    def __init__(self, nombre: str, telefono: str, relacion: str):
        self._nombre = nombre
        self._telefono = telefono
        self._relacion = relacion
    def get_nombre(self) -> str:
        return self._nombre
    def get_telefono(self) -> str:
        return self._telefono
    def get_relacion(self) -> str:
        return self._relacion


