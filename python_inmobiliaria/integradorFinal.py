"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria
Fecha de generacion: 2025-11-04 16:46:18
Total de archivos integrados: 65
Total de directorios procesados: 23
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/contratos
#   4. __init__.py
#   5. contrato.py
#   6. pago.py
#
# DIRECTORIO: entidades/personas
#   7. __init__.py
#   8. garantia.py
#   9. inquilino.py
#   10. propietario.py
#   11. referencia.py
#
# DIRECTORIO: entidades/propiedades
#   12. __init__.py
#   13. casa.py
#   14. departamento.py
#   15. finca.py
#   16. inmueble.py
#   17. propiedad.py
#   18. tipo_amenidad.py
#
# DIRECTORIO: entidades/registros
#   19. __init__.py
#   20. registro_inmobiliario.py
#
# DIRECTORIO: excepciones
#   21. __init__.py
#   22. contrato_vencido_exception.py
#   23. inmobiliaria_exception.py
#   24. mensajes_exception.py
#   25. pago_insuficiente_exception.py
#   26. persistencia_exception.py
#
# DIRECTORIO: monitoreo
#   27. __init__.py
#
# DIRECTORIO: monitoreo/control
#   28. __init__.py
#   29. control_vencimiento_task.py
#
# DIRECTORIO: monitoreo/monitores
#   30. __init__.py
#   31. fecha_monitor_task.py
#   32. pago_monitor_task.py
#
# DIRECTORIO: patrones
#   33. __init__.py
#
# DIRECTORIO: patrones/factory
#   34. __init__.py
#   35. propiedad_factory.py
#
# DIRECTORIO: patrones/observer
#   36. __init__.py
#   37. observable.py
#   38. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   39. __init__.py
#   40. evento_contrato.py
#   41. evento_monitor.py
#
# DIRECTORIO: patrones/singleton
#   42. __init__.py
#
# DIRECTORIO: patrones/strategy
#   43. __init__.py
#   44. ajuste_renta_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   45. __init__.py
#   46. ajuste_fijo_strategy.py
#   47. ajuste_inflacionario_strategy.py
#
# DIRECTORIO: servicios
#   48. __init__.py
#
# DIRECTORIO: servicios/contratos
#   49. __init__.py
#   50. contrato_service.py
#   51. pago_service.py
#
# DIRECTORIO: servicios/negocio
#   52. __init__.py
#   53. inmobiliaria_service.py
#   54. reporte.py
#
# DIRECTORIO: servicios/personas
#   55. __init__.py
#   56. inquilino_service.py
#
# DIRECTORIO: servicios/propiedades
#   57. __init__.py
#   58. casa_service.py
#   59. departamento_service.py
#   60. finca_service.py
#   61. inmueble_service.py
#   62. propiedad_service.py
#   63. propiedad_service_registry.py
#
# DIRECTORIO: servicios/registros
#   64. __init__.py
#   65. registro_inmobiliario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/65: __init__.py
# Directorio: .
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/__init__.py
# ==============================================================================

"""Sistema de Gestion de Arrendamientos y Contratos."""


# ==============================================================================
# ARCHIVO 2/65: constantes.py
# Directorio: .
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/constantes.py
# ==============================================================================

"""
Constantes centralizadas del sistema.

Este modulo contiene todas las constantes utilizadas en el sistema
para evitar valores magicos en el codigo.
"""

# Constantes de propiedades - Casa
SUPERFICIE_MINIMA_CASA = 50.0
VALOR_BASE_CASA = 4000000.0
FACTOR_TERRENO = 1.2
TERRENO_BASE_CASA = 250.0
PLANTAS_BASE_CASA = 2

# Constantes de propiedades - Departamento
SUPERFICIE_MINIMA_DEPTO = 30.0
VALOR_BASE_DEPTO = 2500000.0
FACTOR_PISO = 0.05
PISO_BASE_DEPTO = 5
NUMERO_BASE_DEPTO = 1

# Constantes de propiedades - Finca
SUPERFICIE_MINIMA_FINCA = 10000.0
VALOR_BASE_HECTAREA = 800000.0
TIPO_SUELO_BASE = "productivo"

# Constantes de contratos
DURACION_MINIMA_MESES = 6
DURACION_MAXIMA_MESES = 36
DEPOSITO_GARANTIA_MESES = 2

# Constantes de ajustes
AJUSTE_INFLACION_ANUAL = 1.25
MESES_AJUSTE_CONTRATO = 12

# Constantes de monitoreo
INTERVALO_MONITOR_FECHA = 86400
INTERVALO_MONITOR_PAGO = 3600
DIAS_ALERTA_VENCIMIENTO = 30
INTERVALO_CONTROL_VENCIMIENTO = 86400

# Constantes de threading
THREAD_JOIN_TIMEOUT = 2.0

# Constantes de persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/65: __init__.py
# Directorio: entidades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/__init__.py
# ==============================================================================

"""Entidades del dominio (DTOs)."""



################################################################################
# DIRECTORIO: entidades/contratos
################################################################################

# ==============================================================================
# ARCHIVO 4/65: __init__.py
# Directorio: entidades/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/__init__.py
# ==============================================================================

"""Entidades relacionadas con contratos."""


# ==============================================================================
# ARCHIVO 5/65: contrato.py
# Directorio: entidades/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/contrato.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 6/65: pago.py
# Directorio: entidades/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/contratos/pago.py
# ==============================================================================

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




################################################################################
# DIRECTORIO: entidades/personas
################################################################################

# ==============================================================================
# ARCHIVO 7/65: __init__.py
# Directorio: entidades/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/__init__.py
# ==============================================================================

"""Entidades relacionadas con personas."""


# ==============================================================================
# ARCHIVO 8/65: garantia.py
# Directorio: entidades/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/garantia.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/65: inquilino.py
# Directorio: entidades/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/inquilino.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 10/65: propietario.py
# Directorio: entidades/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/propietario.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/65: referencia.py
# Directorio: entidades/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/personas/referencia.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades/propiedades
################################################################################

# ==============================================================================
# ARCHIVO 12/65: __init__.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/__init__.py
# ==============================================================================

"""Entidades de propiedades inmobiliarias."""


# ==============================================================================
# ARCHIVO 13/65: casa.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/casa.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 14/65: departamento.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/departamento.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 15/65: finca.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/finca.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 16/65: inmueble.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/inmueble.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 17/65: propiedad.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/propiedad.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 18/65: tipo_amenidad.py
# Directorio: entidades/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/propiedades/tipo_amenidad.py
# ==============================================================================

"""Enumeracion de tipos de amenidades."""
# Standard library
from enum import Enum

class TipoAmenidad(Enum):
    """Tipos de amenidades disponibles en departamentos."""
    PISCINA = "Piscina"
    GIMNASIO = "Gimnasio"
    SEGURIDAD = "Seguridad"
    SALON_EVENTOS = "Salon de Eventos"



################################################################################
# DIRECTORIO: entidades/registros
################################################################################

# ==============================================================================
# ARCHIVO 19/65: __init__.py
# Directorio: entidades/registros
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/registros/__init__.py
# ==============================================================================

"""Entidades de registros inmobiliarios."""


# ==============================================================================
# ARCHIVO 20/65: registro_inmobiliario.py
# Directorio: entidades/registros
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/entidades/registros/registro_inmobiliario.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 21/65: __init__.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/__init__.py
# ==============================================================================

"""Excepciones personalizadas del sistema."""


# ==============================================================================
# ARCHIVO 22/65: contrato_vencido_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/contrato_vencido_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 23/65: inmobiliaria_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/inmobiliaria_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 24/65: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/mensajes_exception.py
# ==============================================================================

"""Mensajes centralizados de excepciones."""
MENSAJE_CONTRATO_VENCIDO = "El contrato se encuentra vencido"
MENSAJE_PAGO_INSUFICIENTE = "El monto pagado es insuficiente"
MENSAJE_PERSISTENCIA_ERROR = "Error en operacion de persistencia"
MENSAJE_PROPIETARIO_INVALIDO = "El nombre del propietario no puede ser nulo o vacio"


# ==============================================================================
# ARCHIVO 25/65: pago_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/pago_insuficiente_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 26/65: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/excepciones/persistencia_exception.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: monitoreo
################################################################################

# ==============================================================================
# ARCHIVO 27/65: __init__.py
# Directorio: monitoreo
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/__init__.py
# ==============================================================================

"""Sistema de monitoreo automatizado."""



################################################################################
# DIRECTORIO: monitoreo/control
################################################################################

# ==============================================================================
# ARCHIVO 28/65: __init__.py
# Directorio: monitoreo/control
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/control/__init__.py
# ==============================================================================

"""Controladores de vencimientos."""


# ==============================================================================
# ARCHIVO 29/65: control_vencimiento_task.py
# Directorio: monitoreo/control
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/control/control_vencimiento_task.py
# ==============================================================================

"""Controlador de vencimientos."""
# Standard library
import threading
import time
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import DIAS_ALERTA_VENCIMIENTO, INTERVALO_CONTROL_VENCIMIENTO
from python_inmobiliaria.patrones.observer.observer import Observer
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.monitoreo.monitores.fecha_monitor_task import FechaMonitorTask
    from python_inmobiliaria.monitoreo.monitores.pago_monitor_task import PagoMonitorTask
    from python_inmobiliaria.servicios.contratos.contrato_service import ContratoService

class ControlVencimientoTask(threading.Thread, Observer[date]):
    """Controlador de vencimientos usando patron Observer."""
    def __init__(self, monitor_fecha: 'FechaMonitorTask', monitor_pago: 'PagoMonitorTask', contrato: 'Contrato', contrato_service: 'ContratoService'):
        threading.Thread.__init__(self, daemon=True)
        self._detenido = threading.Event()
        self._fecha_actual = date.today()
        self._contrato = contrato
        self._contrato_service = contrato_service
        monitor_fecha.agregar_observador(self)
    def actualizar(self, evento: date) -> None:
        self._fecha_actual = evento
    def run(self) -> None:
        while not self._detenido.is_set():
            dias_vencimiento = (self._contrato.get_fecha_vencimiento() - self._fecha_actual).days
            if dias_vencimiento <= DIAS_ALERTA_VENCIMIENTO:
                print(f"[ALERTA] Contrato vence en {dias_vencimiento} dias")
            time.sleep(INTERVALO_CONTROL_VENCIMIENTO)
    def detener(self) -> None:
        self._detenido.set()



################################################################################
# DIRECTORIO: monitoreo/monitores
################################################################################

# ==============================================================================
# ARCHIVO 30/65: __init__.py
# Directorio: monitoreo/monitores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/__init__.py
# ==============================================================================

"""Monitores de eventos."""


# ==============================================================================
# ARCHIVO 31/65: fecha_monitor_task.py
# Directorio: monitoreo/monitores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/fecha_monitor_task.py
# ==============================================================================

"""Monitor de fechas."""
# Standard library
import threading
import time
from datetime import date
# Local application
from python_inmobiliaria.constantes import INTERVALO_MONITOR_FECHA
from python_inmobiliaria.patrones.observer.observable import Observable

class FechaMonitorTask(threading.Thread, Observable[date]):
    """Monitor de fechas usando patron Observer."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    def run(self) -> None:
        while not self._detenido.is_set():
            fecha_actual = date.today()
            self.notificar_observadores(fecha_actual)
            time.sleep(INTERVALO_MONITOR_FECHA)
    def detener(self) -> None:
        self._detenido.set()


# ==============================================================================
# ARCHIVO 32/65: pago_monitor_task.py
# Directorio: monitoreo/monitores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/pago_monitor_task.py
# ==============================================================================

"""Monitor de pagos."""
# Standard library
import threading
import time
from typing import List, TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import INTERVALO_MONITOR_PAGO
from python_inmobiliaria.patrones.observer.observable import Observable
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class PagoMonitorTask(threading.Thread, Observable[List['Contrato']]):
    """Monitor de pagos usando patron Observer."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    def run(self) -> None:
        while not self._detenido.is_set():
            contratos_pendientes: List['Contrato'] = []
            self.notificar_observadores(contratos_pendientes)
            time.sleep(INTERVALO_MONITOR_PAGO)
    def detener(self) -> None:
        self._detenido.set()



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 33/65: __init__.py
# Directorio: patrones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/__init__.py
# ==============================================================================

"""Implementaciones de patrones de diseno."""



################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 34/65: __init__.py
# Directorio: patrones/factory
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/factory/__init__.py
# ==============================================================================

"""Patron Factory Method."""


# ==============================================================================
# ARCHIVO 35/65: propiedad_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/factory/propiedad_factory.py
# ==============================================================================

"""Factory Method para creacion de propiedades."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import TERRENO_BASE_CASA, PLANTAS_BASE_CASA, PISO_BASE_DEPTO, NUMERO_BASE_DEPTO, TIPO_SUELO_BASE
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class PropiedadFactory:
    """Factory Method para crear propiedades."""
    @staticmethod
    def crear_propiedad(tipo: str) -> 'Propiedad':
        factories = {
            "Casa": PropiedadFactory._crear_casa,
            "Departamento": PropiedadFactory._crear_departamento,
            "Finca": PropiedadFactory._crear_finca
        }
        if tipo not in factories:
            raise ValueError(f"Tipo de propiedad desconocido: {tipo}")
        return factories[tipo]()
    @staticmethod
    def _crear_casa() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.casa import Casa
        return Casa(terreno=TERRENO_BASE_CASA, plantas=PLANTAS_BASE_CASA, garaje=True)
    @staticmethod
    def _crear_departamento() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.departamento import Departamento
        return Departamento(piso=PISO_BASE_DEPTO, numero=NUMERO_BASE_DEPTO)
    @staticmethod
    def _crear_finca() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.finca import Finca
        return Finca(tipo_suelo=TIPO_SUELO_BASE, acceso_agua=True)



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 36/65: __init__.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/__init__.py
# ==============================================================================

"""Patron Observer."""


# ==============================================================================
# ARCHIVO 37/65: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/observable.py
# ==============================================================================

"""Clase Observable generica."""
# Standard library
from abc import ABC
from typing import Generic, TypeVar, List, TYPE_CHECKING
# Local application
if TYPE_CHECKING:
    from python_inmobiliaria.patrones.observer.observer import Observer
T = TypeVar('T')

class Observable(Generic[T], ABC):
    """Clase Observable generica con tipo-seguridad."""
    def __init__(self):
        self._observadores: List['Observer[T]'] = []
    def agregar_observador(self, observador: 'Observer[T]') -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)
    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)
    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)


# ==============================================================================
# ARCHIVO 38/65: observer.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/observer.py
# ==============================================================================

"""Interfaz Observer generica."""
# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz Observer generica con tipo-seguridad."""
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass



################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 39/65: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/__init__.py
# ==============================================================================

"""Eventos del sistema."""


# ==============================================================================
# ARCHIVO 40/65: evento_contrato.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/evento_contrato.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 41/65: evento_monitor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/eventos/evento_monitor.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 42/65: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/singleton/__init__.py
# ==============================================================================

"""Patron Singleton."""



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 43/65: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/__init__.py
# ==============================================================================

"""Patron Strategy."""


# ==============================================================================
# ARCHIVO 44/65: ajuste_renta_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/ajuste_renta_strategy.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 45/65: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/__init__.py
# ==============================================================================

"""Implementaciones de Strategy."""


# ==============================================================================
# ARCHIVO 46/65: ajuste_fijo_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/ajuste_fijo_strategy.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 47/65: ajuste_inflacionario_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/strategy/impl/ajuste_inflacionario_strategy.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 48/65: __init__.py
# Directorio: servicios
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/__init__.py
# ==============================================================================

"""Servicios de logica de negocio."""



################################################################################
# DIRECTORIO: servicios/contratos
################################################################################

# ==============================================================================
# ARCHIVO 49/65: __init__.py
# Directorio: servicios/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/__init__.py
# ==============================================================================

"""Servicios de contratos."""


# ==============================================================================
# ARCHIVO 50/65: contrato_service.py
# Directorio: servicios/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/contrato_service.py
# ==============================================================================

"""Servicio para contratos."""
# Standard library
from datetime import date, timedelta
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import MESES_AJUSTE_CONTRATO
from python_inmobiliaria.excepciones.contrato_vencido_exception import ContratoVencidoException
from python_inmobiliaria.patrones.strategy.impl.ajuste_inflacionario_strategy import AjusteInflacionarioStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy

class ContratoService:
    """Servicio para contratos con Strategy Pattern."""
    def __init__(self):
        self._estrategia_ajuste: 'AjusteRentaStrategy' = AjusteInflacionarioStrategy()
    def aplicar_ajuste(self, contrato: 'Contrato') -> float:
        if date.today() > contrato.get_fecha_vencimiento():
            raise ContratoVencidoException(contrato.get_fecha_vencimiento(), date.today())
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato.get_monto_mensual(), date.today(), contrato)
        contrato.set_monto_mensual(nuevo_monto)
        return nuevo_monto
    def renovar_contrato(self, contrato_anterior: 'Contrato', duracion_meses: int) -> 'Contrato':
        from python_inmobiliaria.entidades.contratos.contrato import Contrato
        fecha_inicio_nueva = date.today()
        fecha_vencimiento_nueva = fecha_inicio_nueva + timedelta(days=duracion_meses * 30)
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato_anterior.get_monto_mensual(), fecha_inicio_nueva, contrato_anterior)
        nuevo_contrato = Contrato(numero_contrato=contrato_anterior.get_numero_contrato() + 1, fecha_inicio=fecha_inicio_nueva, fecha_vencimiento=fecha_vencimiento_nueva, monto_mensual=nuevo_monto, inquilino=contrato_anterior.get_inquilino(), propiedad=contrato_anterior.get_propiedad())
        return nuevo_contrato


# ==============================================================================
# ARCHIVO 51/65: pago_service.py
# Directorio: servicios/contratos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/pago_service.py
# ==============================================================================

"""Servicio para pagos."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.entidades.contratos.pago import Pago
from python_inmobiliaria.excepciones.pago_insuficiente_exception import PagoInsuficienteException
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class PagoService:
    """Servicio para pagos."""
    def registrar_pago(self, contrato: 'Contrato', monto: float, fecha_pago: date) -> Pago:
        monto_requerido = contrato.get_monto_mensual()
        if monto < monto_requerido:
            raise PagoInsuficienteException(monto_pagado=monto, monto_requerido=monto_requerido, numero_contrato=contrato.get_numero_contrato())
        pago = Pago(monto=monto, fecha_pago=fecha_pago, numero_contrato=contrato.get_numero_contrato())
        return pago



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 52/65: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/__init__.py
# ==============================================================================

"""Servicios de alto nivel."""


# ==============================================================================
# ARCHIVO 53/65: inmobiliaria_service.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/inmobiliaria_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 54/65: reporte.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/negocio/reporte.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/personas
################################################################################

# ==============================================================================
# ARCHIVO 55/65: __init__.py
# Directorio: servicios/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/personas/__init__.py
# ==============================================================================

"""Servicios de personas."""


# ==============================================================================
# ARCHIVO 56/65: inquilino_service.py
# Directorio: servicios/personas
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/personas/inquilino_service.py
# ==============================================================================

"""Servicio para inquilinos."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.entidades.personas.garantia import Garantia
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.entidades.personas.inquilino import Inquilino

class InquilinoService:
    """Servicio para inquilinos."""
    def asignar_garantia(self, inquilino: 'Inquilino', tipo: str, monto: float, fecha_constitucion: date) -> None:
        garantia = Garantia(tipo, monto, fecha_constitucion)
        inquilino.set_garantia(garantia)
    def verificar_garantia(self, inquilino: 'Inquilino') -> bool:
        garantia = inquilino.get_garantia()
        if garantia is None:
            return False
        return garantia.esta_activa()
    def firmar_contrato(self, inquilino: 'Inquilino', contrato: 'Contrato') -> bool:
        if not self.verificar_garantia(inquilino):
            print(f"El inquilino {inquilino.get_nombre()} no tiene garantia valida")
            return False
        print(f"El inquilino {inquilino.get_nombre()} ha firmado el contrato N {contrato.get_numero_contrato()}")
        print(f"Propiedad: {contrato.get_propiedad().get_direccion()}")
        print(f"Monto mensual: ${contrato.get_monto_mensual():,.2f}")
        print(f"Vigencia: {contrato.get_fecha_inicio()} - {contrato.get_fecha_vencimiento()}")
        return True



################################################################################
# DIRECTORIO: servicios/propiedades
################################################################################

# ==============================================================================
# ARCHIVO 57/65: __init__.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/__init__.py
# ==============================================================================

"""Servicios de propiedades."""


# ==============================================================================
# ARCHIVO 58/65: casa_service.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/casa_service.py
# ==============================================================================

"""Servicio para Casa."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import FACTOR_TERRENO
from python_inmobiliaria.servicios.propiedades.inmueble_service import InmuebleService
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.casa import Casa

class CasaService(InmuebleService):
    """Servicio especializado para Casa."""
    def calcular_valor(self, propiedad: 'Casa') -> float:
        valor_base = propiedad.get_valor_base()
        factor = 1.0 + (propiedad.get_terreno() / 1000.0) * FACTOR_TERRENO
        return valor_base * factor
    def mostrar_datos(self, propiedad: 'Casa') -> None:
        super().mostrar_datos(propiedad)
        print(f"Terreno: {propiedad.get_terreno()} m2")
        print(f"Plantas: {propiedad.get_plantas()}")
        print(f"Garaje: {'Si' if propiedad.tiene_garaje() else 'No'}")


# ==============================================================================
# ARCHIVO 59/65: departamento_service.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/departamento_service.py
# ==============================================================================

"""Servicio para Departamento."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import FACTOR_PISO
from python_inmobiliaria.servicios.propiedades.inmueble_service import InmuebleService
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.departamento import Departamento

class DepartamentoService(InmuebleService):
    """Servicio especializado para Departamento."""
    def calcular_valor(self, propiedad: 'Departamento') -> float:
        valor_base = propiedad.get_valor_base()
        factor_piso = 1.0 + (propiedad.get_piso() * FACTOR_PISO)
        return valor_base * factor_piso
    def mostrar_datos(self, propiedad: 'Departamento') -> None:
        super().mostrar_datos(propiedad)
        print(f"Piso: {propiedad.get_piso()}")
        print(f"Numero: {propiedad.get_numero()}")
        amenidades = propiedad.get_amenidades()
        if amenidades:
            print(f"Amenidades: {', '.join(a.value for a in amenidades)}")


# ==============================================================================
# ARCHIVO 60/65: finca_service.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/finca_service.py
# ==============================================================================

"""Servicio para Finca."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.finca import Finca

class FincaService(PropiedadService):
    """Servicio especializado para Finca."""
    def calcular_valor(self, propiedad: 'Finca') -> float:
        hectareas = propiedad.get_superficie() / 10000.0
        valor_por_hectarea = propiedad.get_valor_base()
        factor_agua = 1.2 if propiedad.tiene_acceso_agua() else 1.0
        return hectareas * valor_por_hectarea * factor_agua
    def mostrar_datos(self, propiedad: 'Finca') -> None:
        super().mostrar_datos(propiedad)
        hectareas = propiedad.get_superficie() / 10000.0
        print(f"Extension: {hectareas:.2f} hectareas")
        print(f"Tipo de suelo: {propiedad.get_tipo_suelo()}")
        print(f"Acceso agua: {'Si' if propiedad.tiene_acceso_agua() else 'No'}")


# ==============================================================================
# ARCHIVO 61/65: inmueble_service.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/inmueble_service.py
# ==============================================================================

"""Servicio base para inmuebles."""
# Local application
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService

class InmuebleService(PropiedadService):
    """Servicio base para inmuebles edificados."""
    pass


# ==============================================================================
# ARCHIVO 62/65: propiedad_service.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/propiedad_service.py
# ==============================================================================

"""Servicio base para propiedades."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.patrones.factory.propiedad_factory import PropiedadFactory
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class PropiedadService:
    """Servicio base para propiedades."""
    def registrar_propiedad(self, tipo: str, direccion: str, superficie: float, propietario_dni: int) -> 'Propiedad':
        propiedad = PropiedadFactory.crear_propiedad(tipo)
        propiedad.set_direccion(direccion)
        propiedad.set_superficie(superficie)
        propiedad.set_propietario_dni(propietario_dni)
        return propiedad
    def calcular_valor(self, propiedad: 'Propiedad') -> float:
        return propiedad.get_valor_base()
    def mostrar_datos(self, propiedad: 'Propiedad') -> None:
        print(f"Propiedad: {propiedad.obtener_tipo()}")
        print(f"Direccion: {propiedad.get_direccion()}")
        print(f"Superficie: {propiedad.get_superficie()} m2")


# ==============================================================================
# ARCHIVO 63/65: propiedad_service_registry.py
# Directorio: servicios/propiedades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/propiedad_service_registry.py
# ==============================================================================

"""Registry de servicios de propiedades con patron Singleton."""
# Standard library
from threading import Lock
from typing import TYPE_CHECKING, Dict, Callable
# Local application
from python_inmobiliaria.entidades.propiedades.casa import Casa
from python_inmobiliaria.entidades.propiedades.departamento import Departamento
from python_inmobiliaria.entidades.propiedades.finca import Finca
from python_inmobiliaria.servicios.propiedades.casa_service import CasaService
from python_inmobiliaria.servicios.propiedades.departamento_service import DepartamentoService
from python_inmobiliaria.servicios.propiedades.finca_service import FincaService
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class PropiedadServiceRegistry:
    """Registry de servicios con patron Singleton."""
    _instance = None
    _lock = Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance
    @classmethod
    def get_instance(cls) -> 'PropiedadServiceRegistry':
        if cls._instance is None:
            cls()
        return cls._instance
    def _inicializar_servicios(self) -> None:
        self._casa_service = CasaService()
        self._departamento_service = DepartamentoService()
        self._finca_service = FincaService()
        self._calcular_valor_handlers: Dict[type, Callable] = {
            Casa: self._calcular_valor_casa,
            Departamento: self._calcular_valor_departamento,
            Finca: self._calcular_valor_finca
        }
        self._mostrar_datos_handlers: Dict[type, Callable] = {
            Casa: self._mostrar_datos_casa,
            Departamento: self._mostrar_datos_departamento,
            Finca: self._mostrar_datos_finca
        }
    def calcular_valor(self, propiedad: 'Propiedad') -> float:
        tipo = type(propiedad)
        if tipo not in self._calcular_valor_handlers:
            raise ValueError(f"Tipo no registrado: {tipo}")
        return self._calcular_valor_handlers[tipo](propiedad)
    def mostrar_datos(self, propiedad: 'Propiedad') -> None:
        tipo = type(propiedad)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](propiedad)
    def _calcular_valor_casa(self, propiedad: Casa) -> float:
        return self._casa_service.calcular_valor(propiedad)
    def _calcular_valor_departamento(self, propiedad: Departamento) -> float:
        return self._departamento_service.calcular_valor(propiedad)
    def _calcular_valor_finca(self, propiedad: Finca) -> float:
        return self._finca_service.calcular_valor(propiedad)
    def _mostrar_datos_casa(self, propiedad: Casa) -> None:
        self._casa_service.mostrar_datos(propiedad)
    def _mostrar_datos_departamento(self, propiedad: Departamento) -> None:
        self._departamento_service.mostrar_datos(propiedad)
    def _mostrar_datos_finca(self, propiedad: Finca) -> None:
        self._finca_service.mostrar_datos(propiedad)



################################################################################
# DIRECTORIO: servicios/registros
################################################################################

# ==============================================================================
# ARCHIVO 64/65: __init__.py
# Directorio: servicios/registros
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/registros/__init__.py
# ==============================================================================

"""Servicios de registros."""


# ==============================================================================
# ARCHIVO 65/65: registro_inmobiliario_service.py
# Directorio: servicios/registros
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/registros/registro_inmobiliario_service.py
# ==============================================================================

"""Servicio para registros inmobiliarios."""
# Standard library
import os
import pickle
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_inmobiliaria.excepciones.persistencia_exception import PersistenciaException, TipoOperacion
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

class RegistroInmobiliarioService:
    """Servicio para registros inmobiliarios con persistencia."""
    def persistir(self, registro: 'RegistroInmobiliario') -> None:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        propietario = registro.get_propietario()
        tipo_propiedad = registro.get_propiedad().obtener_tipo()
        nombre_archivo = f"{propietario.replace(' ', '_')}_{tipo_propiedad}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        archivo = None
        try:
            archivo = open(ruta_completa, 'wb')
            pickle.dump(registro, archivo)
            print(f"Registro de {propietario} ({tipo_propiedad}) persistido exitosamente en {ruta_completa}")
        except Exception as e:
            raise PersistenciaException(tipo_operacion=TipoOperacion.ESCRITURA, nombre_archivo=ruta_completa, causa=str(e))
        finally:
            if archivo:
                archivo.close()
    @staticmethod
    def leer_registro(propietario: str, tipo_propiedad: str) -> 'RegistroInmobiliario':
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")
        nombre_archivo = f"{propietario.replace(' ', '_')}_{tipo_propiedad}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        if not os.path.exists(ruta_completa):
            raise PersistenciaException(tipo_operacion=TipoOperacion.LECTURA, nombre_archivo=ruta_completa, causa="Archivo no encontrado")
        archivo = None
        try:
            archivo = open(ruta_completa, 'rb')
            registro = pickle.load(archivo)
            print(f"Registro de {propietario} ({tipo_propiedad}) recuperado exitosamente desde {ruta_completa}")
            return registro
        except Exception as e:
            raise PersistenciaException(tipo_operacion=TipoOperacion.LECTURA, nombre_archivo=ruta_completa, causa=str(e))
        finally:
            if archivo:
                archivo.close()
    def mostrar_datos(self, registro: 'RegistroInmobiliario') -> None:
        print()
        print("REGISTRO INMOBILIARIO")
        print("=" * 50)
        print(f"ID Registro:  {registro.get_id_registro()}")
        print(f"Propietario:  {registro.get_propietario()}")
        print(f"Valor Fiscal: {registro.get_valor_fiscal()}")
        print(f"Direccion:    {registro.get_propiedad().get_direccion()}")
        print(f"Superficie:   {registro.get_propiedad().get_superficie()} m2")
        print(f"Monto mensual: ${registro.get_contrato().get_monto_mensual():,.2f}")



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 65
# Generado: 2025-11-04 16:46:18
################################################################################
