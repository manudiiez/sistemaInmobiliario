"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/__init__.py
# ================================================================================

"""Servicios de contratos."""


# ================================================================================
# ARCHIVO 2/3: contrato_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/contrato_service.py
# ================================================================================

"""Servicio para contratos."""
# Standard library
from datetime import date, timedelta
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import MESES_AJUSTE_CONTRATO
from python_inmobiliaria.excepciones.contrato_vencido_exception import ContratoVencidoException
from python_inmobiliaria.patrones.strategy.impl.ajuste_inflacionario_strategy import AjusteInflacionarioStrategy
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.patrones.strategy.ajuste_renta_strategy import AjusteRentaStrategy

class ContratoService:
    """Servicio para contratos con Strategy Pattern."""
    def __init__(self):
        self._estrategia_ajuste: 'AjusteRentaStrategy' = AjusteInflacionarioStrategy()
    def aplicar_ajuste(self, contrato: 'Contrato') -> float:
        if date.today() > contrato.get_fecha_vencimiento():
            raise ContratoVencidoException(contrato.get_fecha_vencimiento(), date.today())
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato.get_monto_mensual(), date.today(), contrato)
        contrato.set_monto_mensual(nuevo_monto)
        return nuevo_monto
    def renovar_contrato(self, contrato_anterior: 'Contrato', duracion_meses: int) -> 'Contrato':
        from python_inmobiliaria.entidades.contratos.contrato import Contrato
        fecha_inicio_nueva = date.today()
        fecha_vencimiento_nueva = fecha_inicio_nueva + timedelta(days=duracion_meses * 30)
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(contrato_anterior.get_monto_mensual(), fecha_inicio_nueva, contrato_anterior)
        nuevo_contrato = Contrato(numero_contrato=contrato_anterior.get_numero_contrato() + 1, fecha_inicio=fecha_inicio_nueva, fecha_vencimiento=fecha_vencimiento_nueva, monto_mensual=nuevo_monto, inquilino=contrato_anterior.get_inquilino(), propiedad=contrato_anterior.get_propiedad())
        return nuevo_contrato


# ================================================================================
# ARCHIVO 3/3: pago_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/servicios/contratos/pago_service.py
# ================================================================================

"""Servicio para pagos."""
# Standard library
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.entidades.contratos.pago import Pago
from python_inmobiliaria.excepciones.pago_insuficiente_exception import PagoInsuficienteException
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class PagoService:
    """Servicio para pagos."""
    def registrar_pago(self, contrato: 'Contrato', monto: float, fecha_pago: date) -> Pago:
        monto_requerido = contrato.get_monto_mensual()
        if monto < monto_requerido:
            raise PagoInsuficienteException(monto_pagado=monto, monto_requerido=monto_requerido, numero_contrato=contrato.get_numero_contrato())
        pago = Pago(monto=monto, fecha_pago=fecha_pago, numero_contrato=contrato.get_numero_contrato())
        return pago


