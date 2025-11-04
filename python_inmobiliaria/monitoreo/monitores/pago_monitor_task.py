"""Monitor de pagos."""
# Standard library
import threading
import time
from typing import List, TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import INTERVALO_MONITOR_PAGO
from python_inmobiliaria.patrones.observer.observable import Observable
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.contratos.contrato import Contrato

class PagoMonitorTask(threading.Thread, Observable[List['Contrato']]):
    """Monitor de pagos usando patron Observer."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    def run(self) -> None:
        while not self._detenido.is_set():
            contratos_pendientes: List['Contrato'] = []
            self.notificar_observadores(contratos_pendientes)
            time.sleep(INTERVALO_MONITOR_PAGO)
    def detener(self) -> None:
        self._detenido.set()
