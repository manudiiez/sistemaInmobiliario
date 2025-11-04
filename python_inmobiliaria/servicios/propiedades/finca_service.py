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
