"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/__init__.py
# ================================================================================

"""Servicios de propiedades."""


# ================================================================================
# ARCHIVO 2/7: casa_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/casa_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/7: departamento_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/departamento_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/7: finca_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/finca_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/7: inmueble_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/inmueble_service.py
# ================================================================================

"""Servicio base para inmuebles."""
# Local application
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService

class InmuebleService(PropiedadService):
    """Servicio base para inmuebles edificados."""
    pass


# ================================================================================
# ARCHIVO 6/7: propiedad_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/propiedad_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/7: propiedad_service_registry.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/propiedades/propiedad_service_registry.py
# ================================================================================

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


