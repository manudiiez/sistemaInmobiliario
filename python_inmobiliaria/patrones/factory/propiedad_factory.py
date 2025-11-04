"""Factory Method para creacion de propiedades."""
# Standard library
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import TERRENO_BASE_CASA, PLANTAS_BASE_CASA, PISO_BASE_DEPTO, NUMERO_BASE_DEPTO, TIPO_SUELO_BASE
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.propiedades.propiedad import Propiedad

class PropiedadFactory:
    """Factory Method para crear propiedades."""
    @staticmethod
    def crear_propiedad(tipo: str) -> 'Propiedad':
        factories = {
            "Casa": PropiedadFactory._crear_casa,
            "Departamento": PropiedadFactory._crear_departamento,
            "Finca": PropiedadFactory._crear_finca
        }
        if tipo not in factories:
            raise ValueError(f"Tipo de propiedad desconocido: {tipo}")
        return factories[tipo]()
    @staticmethod
    def _crear_casa() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.casa import Casa
        return Casa(terreno=TERRENO_BASE_CASA, plantas=PLANTAS_BASE_CASA, garaje=True)
    @staticmethod
    def _crear_departamento() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.departamento import Departamento
        return Departamento(piso=PISO_BASE_DEPTO, numero=NUMERO_BASE_DEPTO)
    @staticmethod
    def _crear_finca() -> 'Propiedad':
        from python_inmobiliaria.entidades.propiedades.finca import Finca
        return Finca(tipo_suelo=TIPO_SUELO_BASE, acceso_agua=True)
