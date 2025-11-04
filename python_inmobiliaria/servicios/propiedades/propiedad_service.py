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
