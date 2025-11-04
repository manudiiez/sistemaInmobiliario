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
