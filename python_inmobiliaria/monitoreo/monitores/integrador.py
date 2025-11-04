"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores
Fecha: 2025-11-04 16:46:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/__init__.py
# ================================================================================

"""Monitores de eventos."""


# ================================================================================
# ARCHIVO 2/3: fecha_monitor_task.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/fecha_monitor_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: pago_monitor_task.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/sistemaInmobiliario/python_inmobiliaria_proyecto/python_inmobiliaria/monitoreo/monitores/pago_monitor_task.py
# ================================================================================

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


