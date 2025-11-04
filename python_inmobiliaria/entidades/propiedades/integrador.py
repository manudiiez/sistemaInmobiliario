"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/__init__.py
# ================================================================================

"""Entidades de propiedades inmobiliarias."""


# ================================================================================
# ARCHIVO 2/7: casa.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/casa.py
# ================================================================================

"""
Entidad Casa - Propiedad unifamiliar.

Este modulo define la entidad Casa con sus caracteristicas especificas
como terreno, plantas y garaje.
"""

# Local application
from python_inmobiliaria.constantes import (
    VALOR_BASE_CASA,
    SUPERFICIE_MINIMA_CASA,
    TERRENO_BASE_CASA,
    PLANTAS_BASE_CASA
)
from python_inmobiliaria.entidades.propiedades.inmueble import Inmueble


class Casa(Inmueble):
    """Entidad Casa - solo contiene datos."""

    def __init__(self, terreno: float, plantas: int, garaje: bool):
        """
        Inicializa una casa.

        Args:
            terreno: Metros cuadrados de terreno
            plantas: Cantidad de plantas
            garaje: Indica si tiene garaje
        """
        super().__init__(
            valor_base=VALOR_BASE_CASA,
            superficie=SUPERFICIE_MINIMA_CASA
        )
        self._terreno = terreno
        self._plantas = plantas
        self._garaje = garaje

    def get_terreno(self) -> float:
        """Retorna los metros de terreno."""
        return self._terreno

    def set_terreno(self, terreno: float) -> None:
        """Establece los metros de terreno."""
        self._terreno = terreno

    def get_plantas(self) -> int:
        """Retorna la cantidad de plantas."""
        return self._plantas

    def set_plantas(self, plantas: int) -> None:
        """Establece la cantidad de plantas."""
        self._plantas = plantas

    def tiene_garaje(self) -> bool:
        """Retorna si tiene garaje."""
        return self._garaje

    def set_garaje(self, garaje: bool) -> None:
        """Establece si tiene garaje."""
        self._garaje = garaje

    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de propiedad.

        Returns:
            Tipo Casa
        """
        return "Casa"


# ================================================================================
# ARCHIVO 3/7: departamento.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/departamento.py
# ================================================================================

"""Entidad Departamento - Unidad en edificio."""

# Standard library
from typing import TYPE_CHECKING, List
# Local application
from python_inmobiliaria.constantes import VALOR_BASE_DEPTO, SUPERFICIE_MINIMA_DEPTO, PISO_BASE_DEPTO, NUMERO_BASE_DEPTO
from python_inmobiliaria.entidades.propiedades.inmueble import Inmueble
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.tipo_amenidad import TipoAmenidad

class Departamento(Inmueble):
    """Entidad Departamento - solo contiene datos."""
    def __init__(self, piso: int, numero: int):
        super().__init__(valor_base=VALOR_BASE_DEPTO, superficie=SUPERFICIE_MINIMA_DEPTO)
        self._piso = piso
        self._numero = numero
        self._amenidades: List[TipoAmenidad] = []
    def get_piso(self) -> int:
        return self._piso
    def set_piso(self, piso: int) -> None:
        self._piso = piso
    def get_numero(self) -> int:
        return self._numero
    def set_numero(self, numero: int) -> None:
        self._numero = numero
    def get_amenidades(self) -> List['TipoAmenidad']:
        return self._amenidades.copy()
    def agregar_amenidad(self, amenidad: 'TipoAmenidad') -> None:
        if amenidad not in self._amenidades:
            self._amenidades.append(amenidad)
    def obtener_tipo(self) -> str:
        return "Departamento"


# ================================================================================
# ARCHIVO 4/7: finca.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/finca.py
# ================================================================================

"""Entidad Finca - Propiedad rural."""

# Local application
from python_inmobiliaria.constantes import VALOR_BASE_HECTAREA, SUPERFICIE_MINIMA_FINCA, TIPO_SUELO_BASE
from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class Finca(Propiedad):
    """Entidad Finca - solo contiene datos."""
    def __init__(self, tipo_suelo: str, acceso_agua: bool):
        super().__init__(valor_base=VALOR_BASE_HECTAREA, superficie=SUPERFICIE_MINIMA_FINCA)
        self._tipo_suelo = tipo_suelo
        self._acceso_agua = acceso_agua
    def get_tipo_suelo(self) -> str:
        return self._tipo_suelo
    def set_tipo_suelo(self, tipo_suelo: str) -> None:
        self._tipo_suelo = tipo_suelo
    def tiene_acceso_agua(self) -> bool:
        return self._acceso_agua
    def set_acceso_agua(self, acceso_agua: bool) -> None:
        self._acceso_agua = acceso_agua
    def obtener_tipo(self) -> str:
        return "Finca"


# ================================================================================
# ARCHIVO 5/7: inmueble.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/inmueble.py
# ================================================================================

"""
Clase base para inmuebles edificados.

Este modulo define la clase base para propiedades que son construcciones
como casas y departamentos.
"""

# Local application
from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad


class Inmueble(Propiedad):
    """Clase base para inmuebles edificados (Casa, Departamento)."""

    def __init__(self, valor_base: float, superficie: float):
        """
        Inicializa un inmueble.

        Args:
            valor_base: Valor base del inmueble
            superficie: Superficie en metros cuadrados
        """
        super().__init__(valor_base, superficie)

    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de inmueble.

        Returns:
            Tipo generico Inmueble
        """
        return "Inmueble"


# ================================================================================
# ARCHIVO 6/7: propiedad.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/propiedad.py
# ================================================================================

"""
Interfaz base para todas las propiedades inmobiliarias.

Este modulo define la interfaz abstracta que todas las propiedades
deben implementar.
"""
# Standard library
from abc import ABC, abstractmethod


class Propiedad(ABC):
    """Interfaz base abstracta para propiedades inmobiliarias."""

    def __init__(self, valor_base: float, superficie: float):
        """
        Inicializa una propiedad.

        Args:
            valor_base: Valor base de la propiedad
            superficie: Superficie en metros cuadrados

        Raises:
            ValueError: Si superficie es menor o igual a cero
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        
        self._valor_base = valor_base
        self._superficie = superficie
        self._direccion = ""
        self._propietario_dni = 0

    def get_valor_base(self) -> float:
        """Retorna el valor base de la propiedad."""
        return self._valor_base

    def set_valor_base(self, valor_base: float) -> None:
        """Establece el valor base de la propiedad."""
        self._valor_base = valor_base

    def get_superficie(self) -> float:
        """Retorna la superficie de la propiedad."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie de la propiedad.

        Args:
            superficie: Superficie en metros cuadrados

        Raises:
            ValueError: Si superficie es menor o igual a cero
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_direccion(self) -> str:
        """Retorna la direccion de la propiedad."""
        return self._direccion

    def set_direccion(self, direccion: str) -> None:
        """Establece la direccion de la propiedad."""
        self._direccion = direccion

    def get_propietario_dni(self) -> int:
        """Retorna el DNI del propietario."""
        return self._propietario_dni

    def set_propietario_dni(self, propietario_dni: int) -> None:
        """Establece el DNI del propietario."""
        self._propietario_dni = propietario_dni

    @abstractmethod
    def obtener_tipo(self) -> str:
        """
        Retorna el tipo de propiedad.

        Returns:
            Tipo de propiedad como string
        """
        pass


# ================================================================================
# ARCHIVO 7/7: tipo_amenidad.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/tipo_amenidad.py
# ================================================================================

"""Enumeracion de tipos de amenidades."""
# Standard library
from enum import Enum

class TipoAmenidad(Enum):
    """Tipos de amenidades disponibles en departamentos."""
    PISCINA = "Piscina"
    GIMNASIO = "Gimnasio"
    SEGURIDAD = "Seguridad"
    SALON_EVENTOS = "Salon de Eventos"


