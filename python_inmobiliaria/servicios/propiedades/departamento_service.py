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
