"""
Sistema de Gestion de Arrendamientos y Contratos - Demostracion completa.

Este modulo demuestra la implementacion de multiples patrones de diseno
en un sistema de gestion inmobiliaria.
"""

# Standard library
import time
from datetime import date, timedelta
# Local application
from python_inmobiliaria.constantes import THREAD_JOIN_TIMEOUT
from python_inmobiliaria.entidades.contratos.contrato import Contrato
from python_inmobiliaria.entidades.personas.inquilino import Inquilino
from python_inmobiliaria.entidades.personas.referencia import Referencia
from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario
from python_inmobiliaria.monitoreo.control.control_vencimiento_task import ControlVencimientoTask
from python_inmobiliaria.monitoreo.monitores.fecha_monitor_task import FechaMonitorTask
from python_inmobiliaria.monitoreo.monitores.pago_monitor_task import PagoMonitorTask
from python_inmobiliaria.servicios.contratos.contrato_service import ContratoService
from python_inmobiliaria.servicios.negocio.inmobiliaria_service import InmobiliariaService
from python_inmobiliaria.servicios.personas.inquilino_service import InquilinoService
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService
from python_inmobiliaria.servicios.propiedades.propiedad_service_registry import PropiedadServiceRegistry
from python_inmobiliaria.servicios.registros.registro_inmobiliario_service import RegistroInmobiliarioService


def main() -> None:
    """Funcion principal que ejecuta la demostracion completa del sistema."""
    print("=" * 70)
    print("      SISTEMA DE GESTION DE ARRENDAMIENTOS Y CONTRATOS")
    print("=" * 70)
    print()

    # PATRON SINGLETON: Demostrar instancia unica
    print("-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)
    registry1 = PropiedadServiceRegistry()
    registry2 = PropiedadServiceRegistry.get_instance()
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    print()

    # PATRON FACTORY: Registrar propiedades
    print("1. Registrando propiedades...")
    propiedad_service = PropiedadService()
    
    casa = propiedad_service.registrar_propiedad(
        tipo="Casa",
        direccion="Av. San Martin 1500",
        superficie=150.0,
        propietario_dni=12345678
    )
    
    departamento = propiedad_service.registrar_propiedad(
        tipo="Departamento",
        direccion="Torre Mirador - Piso 8 - Depto 2",
        superficie=75.0,
        propietario_dni=23456789
    )
    
    finca = propiedad_service.registrar_propiedad(
        tipo="Finca",
        direccion="Ruta 40 Km 1250 - Uspallata",
        superficie=50000.0,
        propietario_dni=34567890
    )
    print("[OK] 3 propiedades registradas usando FACTORY METHOD")
    print()

    # Crear contrato
    print("2. Creando contrato de arrendamiento...")
    contrato_service = ContratoService()
    
    # Crear inquilino con referencias
    referencias = [
        Referencia("Carlos Lopez", "261-4567890", "Laboral"),
        Referencia("Ana Martinez", "261-7891234", "Personal")
    ]
    
    inquilino = Inquilino(
        dni=43888734,
        nombre="Juan Perez",
        telefono="261-9876543",
        referencias=referencias
    )
    
    # Asignar garantia
    inquilino_service = InquilinoService()
    inquilino_service.asignar_garantia(
        inquilino=inquilino,
        tipo="Deposito",
        monto=100000.0,
        fecha_constitucion=date.today()
    )
    
    # Firmar contrato
    contrato = Contrato(
        numero_contrato=1,
        fecha_inicio=date.today(),
        fecha_vencimiento=date.today() + timedelta(days=365),
        monto_mensual=50000.0,
        inquilino=inquilino,
        propiedad=casa
    )
    
    inquilino_service.firmar_contrato(inquilino, contrato)
    print("[OK] Contrato firmado exitosamente")
    print()

    # Crear registro inmobiliario
    print("3. Creando registro inmobiliario...")
    registro = RegistroInmobiliario(
        id_registro=1,
        propiedad=casa,
        contrato=contrato,
        propietario="Maria Gonzalez",
        valor_fiscal=5500000.00
    )
    print("[OK] Registro creado")
    print()

    # PATRON STRATEGY: Aplicar ajuste
    print("4. Aplicando ajuste de renta con STRATEGY...")
    contrato_service.aplicar_ajuste(contrato)
    print(f"[OK] Nuevo monto: ${contrato.get_monto_mensual():,.2f}")
    print()

    # PATRON OBSERVER: Sistema de monitoreo
    print("5. Iniciando sistema de monitoreo con OBSERVER...")
    tarea_fecha = FechaMonitorTask()
    tarea_pago = PagoMonitorTask()
    tarea_control = ControlVencimientoTask(
        tarea_fecha,
        tarea_pago,
        contrato,
        contrato_service
    )
    
    tarea_fecha.start()
    tarea_pago.start()
    tarea_control.start()
    print("[OK] Monitores activos (threads daemon)")
    print()

    # Dejar funcionar el sistema
    print("6. Sistema funcionando durante 5 segundos...")
    time.sleep(5)
    
    # Detener monitores
    print("7. Deteniendo monitores...")
    tarea_fecha.detener()
    tarea_pago.detener()
    tarea_control.detener()
    
    tarea_fecha.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_pago.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)
    print("[OK] Monitores detenidos correctamente")
    print()

    # Persistencia
    print("8. Persistiendo datos...")
    registro_service = RegistroInmobiliarioService()
    registro_service.persistir(registro)
    print("[OK] Registro persistido")
    print()

    # Recuperar datos
    print("9. Recuperando datos persistidos...")
    registro_leido = RegistroInmobiliarioService.leer_registro("Maria Gonzalez", "Casa")
    registro_service.mostrar_datos(registro_leido)
    print()

    print("=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - PropiedadServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de propiedades")
    print("  [OK] OBSERVER    - Sistema de monitoreo y eventos")
    print("  [OK] STRATEGY    - Algoritmos de ajuste de renta")
    print("=" * 70)


if __name__ == "__main__":
    main()
