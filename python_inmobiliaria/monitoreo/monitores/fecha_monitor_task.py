"""Monitor de fechas."""
# Standard library
import threading
import time
from datetime import date
# Local application
from python_inmobiliaria.constantes import INTERVALO_MONITOR_FECHA
from python_inmobiliaria.patrones.observer.observable import Observable

class FechaMonitorTask(threading.Thread, Observable[date]):
    """Monitor de fechas usando patron Observer."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    def run(self) -> None:
        while not self._detenido.is_set():
            fecha_actual = date.today()
            self.notificar_observadores(fecha_actual)
            time.sleep(INTERVALO_MONITOR_FECHA)
    def detener(self) -> None:
        self._detenido.set()
