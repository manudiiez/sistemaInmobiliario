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
