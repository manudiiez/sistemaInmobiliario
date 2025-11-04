"""Servicio para inquilinos."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.entidades.personas.garantia import Garantia
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.entidades.personas.inquilino import Inquilino

class InquilinoService:
    """Servicio para inquilinos."""
    def asignar_garantia(self, inquilino: 'Inquilino', tipo: str, monto: float, fecha_constitucion: date) -> None:
        garantia = Garantia(tipo, monto, fecha_constitucion)
        inquilino.set_garantia(garantia)
    def verificar_garantia(self, inquilino: 'Inquilino') -> bool:
        garantia = inquilino.get_garantia()
        if garantia is None:
            return False
        return garantia.esta_activa()
    def firmar_contrato(self, inquilino: 'Inquilino', contrato: 'Contrato') -> bool:
        if not self.verificar_garantia(inquilino):
            print(f"El inquilino {inquilino.get_nombre()} no tiene garantia valida")
            return False
        print(f"El inquilino {inquilino.get_nombre()} ha firmado el contrato N {contrato.get_numero_contrato()}")
        print(f"Propiedad: {contrato.get_propiedad().get_direccion()}")
        print(f"Monto mensual: ${contrato.get_monto_mensual():,.2f}")
        print(f"Vigencia: {contrato.get_fecha_inicio()} - {contrato.get_fecha_vencimiento()}")
        return True
