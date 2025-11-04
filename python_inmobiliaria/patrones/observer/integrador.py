"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/__init__.py
# ================================================================================

"""Patron Observer."""


# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/patrones/observer/observer.py
# ================================================================================

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


