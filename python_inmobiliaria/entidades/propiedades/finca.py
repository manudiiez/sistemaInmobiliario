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
