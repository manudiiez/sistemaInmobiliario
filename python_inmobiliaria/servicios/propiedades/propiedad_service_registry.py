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
