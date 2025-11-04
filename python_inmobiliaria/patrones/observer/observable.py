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
