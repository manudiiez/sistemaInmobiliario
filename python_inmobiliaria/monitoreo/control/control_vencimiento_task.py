"""Controlador de vencimientos."""
# Standard library
import threading
import time
from datetime import date
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import DIAS_ALERTA_VENCIMIENTO, INTERVALO_CONTROL_VENCIMIENTO
from python_inmobiliaria.patrones.observer.observer import Observer
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato
    from python_inmobiliaria.monitoreo.monitores.fecha_monitor_task import FechaMonitorTask
    from python_inmobiliaria.monitoreo.monitores.pago_monitor_task import PagoMonitorTask
    from python_inmobiliaria.servicios.contratos.contrato_service import ContratoService

class ControlVencimientoTask(threading.Thread, Observer[date]):
    """Controlador de vencimientos usando patron Observer."""
    def __init__(self, monitor_fecha: 'FechaMonitorTask', monitor_pago: 'PagoMonitorTask', contrato: 'Contrato', contrato_service: 'ContratoService'):
        threading.Thread.__init__(self, daemon=True)
        self._detenido = threading.Event()
        self._fecha_actual = date.today()
        self._contrato = contrato
        self._contrato_service = contrato_service
        monitor_fecha.agregar_observador(self)
    def actualizar(self, evento: date) -> None:
        self._fecha_actual = evento
    def run(self) -> None:
        while not self._detenido.is_set():
            dias_vencimiento = (self._contrato.get_fecha_vencimiento() - self._fecha_actual).days
            if dias_vencimiento <= DIAS_ALERTA_VENCIMIENTO:
                print(f"[ALERTA] Contrato vence en {dias_vencimiento} dias")
            time.sleep(INTERVALO_CONTROL_VENCIMIENTO)
    def detener(self) -> None:
        self._detenido.set()
