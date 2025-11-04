# Sistema de Gestión de Arrendamientos y Contratos

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestión inmobiliaria para administración de arrendamientos y contratos que demuestra la implementación de múltiples patrones de diseño de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#características-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseño-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Módulos del Sistema](#módulos-del-sistema)
- [Documentación Técnica](#documentación-técnica)
- [Testing y Validación](#testing-y-validación)
- [Contribución](#contribución)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **PythonInmobiliaria** aborda los desafíos de la gestión moderna de arrendamientos y contratos inmobiliarios, un dominio que requiere:

1. **Gestión de Múltiples Tipos de Propiedades**
    - Casas unifamiliares con características específicas
    - Departamentos en edificios con amenidades compartidas
    - Fincas y propiedades rurales con extensiones variables
    - Cada tipo con requisitos y valuaciones particulares

2. **Monitoreo de Contratos y Vencimientos en Tiempo Real**
    - Sistema de alertas para vencimientos de contratos
    - Control automático de fechas de renovación
    - Notificaciones de pagos vencidos o próximos a vencer
    - Respuesta dinámica a cambios en condiciones contractuales

3. **Gestión de Personas (Inquilinos y Propietarios)**
    - Control de inquilinos con documentación completa
    - Registro de propietarios con múltiples propiedades
    - Historial de comportamiento de pago
    - Referencias y garantías asociadas

4. **Planificación Financiera**
    - Optimización de ingresos por alquileres
    - Control de morosidad y deudas
    - Proyección de ingresos futuros
    - Cálculo automático de ajustes por inflación

5. **Persistencia y Trazabilidad**
    - Almacenamiento permanente de registros contractuales
    - Recuperación de históricos para auditoría
    - Generación de reportes financieros
    - Cumplimiento de normativas legales

### Actores del Sistema

- **Administrador Inmobiliario**: Gestiona el portafolio completo, supervisa operaciones
- **Propietario**: Dueño de propiedades, consulta estados y recibe pagos
- **Inquilino**: Persona que alquila, realiza pagos y reporta mantenimientos
- **Sistema de Alertas Automatizado**: Opera de forma autónoma basado en fechas y eventos
- **Auditor/Contador**: Consulta registros financieros para declaraciones

### Flujo de Operaciones Típico

```
1. REGISTRO --> Se registra una propiedad con su propietario
2. CONTRATO --> Se crea un contrato vinculando inquilino y propiedad
3. MONITOREO --> Sistema detecta fechas de pago y vencimientos
4. COBRO AUTOMÁTICO --> Sistema genera recordatorios y registra pagos
5. AJUSTE --> Contratos se actualizan según cláusulas de ajuste
6. MANTENIMIENTO --> Se registran y gestionan reclamos
7. RENOVACIÓN --> Contratos se renuevan o finalizan automáticamente
8. PERSISTENCIA --> Datos se guardan para auditoría futura
```

---

## Características Principales

### Funcionalidades del Sistema

#### 1. Gestión de Propiedades

- **Creación dinámica** de 3 tipos de propiedades mediante Factory Pattern
    - **Casa**: Propiedad unifamiliar con terreno y características específicas
    - **Departamento**: Unidad en edificio con piso, número y amenidades
    - **Finca**: Propiedad rural con extensión y características agrícolas

- **Características diferenciadas** por tipo
    - Casas: Metros de terreno, cantidad de plantas, garaje
    - Departamentos: Piso, número, amenidades (piscina, gimnasio)
    - Fincas: Hectáreas, tipo de suelo, acceso a agua

- **Valuación automática** para propiedades
    - Casa: Basada en ubicación y características
    - Departamento: Según piso y amenidades
    - Finca: Por extensión y productividad

#### 2. Sistema de Contratos Inteligente

- **Contratos en tiempo real** (patrón Observer)
    - Monitoreo de fechas de vencimiento
    - Alertas de pagos próximos cada día
    - Control de renovaciones automáticas

- **Gestión automatizada condicional**
    - Se activa cuando:
        - Fecha actual >= Fecha de pago, O
        - Días para vencimiento <= 30
    - Control diario de estados

- **Notificaciones de eventos**
    - Eventos de contratos a observadores suscritos
    - Sistema tipo-seguro con Generics (Observable[Contrato])

#### 3. Gestión de Personas

- **Inquilinos con documentación completa**
    - DNI, nombre completo, contacto
    - Historial de pagos
    - Referencias personales
    - Estado de morosidad

- **Sistema de garantías**
    - Depósito de garantía obligatorio
    - Validación automática antes de contrato
    - Fecha de emisión y monto
    - Estado de devolución

- **Propietarios con múltiples propiedades**
    - ID único, nombre y datos bancarios
    - Lista de propiedades asociadas
    - Historial de ingresos

#### 4. Gestión Contractual

- **Contrato**
    - Número único de contrato
    - Fecha de inicio y vencimiento
    - Monto mensual y forma de pago
    - Cláusulas de ajuste

- **Inquilino**
    - Vinculación con contrato activo
    - Historial de contratos anteriores
    - Comportamiento de pago
    - Estado actual (activo/inactivo)

- **Propiedad Arrendada**
    - Estado (disponible/ocupada/en mantenimiento)
    - Contrato actual vigente
    - Historial de contratos anteriores
    - Última fecha de inspección

#### 5. Operaciones de Negocio

- **Registro automático de propiedades**
    - Cálculo de valor estimado
    - Validación de datos catastrales
    - Creación vía Factory Method

- **Gestión de pagos**
    - Registra pagos de inquilinos
    - Verifica montos y fechas
    - Excepción si pago insuficiente

- **Renovaciones automáticas**
    - Renovación selectiva por contrato
    - Aplicación de ajustes contractuales
    - Generación de nuevo contrato

- **Mantenimiento**
    - Registro de reclamos por propiedad
    - Asignación de prioridad
    - Seguimiento de resolución

#### 6. Persistencia de Datos

- **Serialización con Pickle**
    - Guardado completo de RegistroInmobiliario
    - Directorio configurable (default: `data/`)
    - Nombre de archivo: `{propietario}_{propiedad}.dat`

- **Recuperación de datos**
    - Lectura de registros persistidos
    - Validación de integridad
    - Manejo de excepciones específicas

---

## Arquitectura del Sistema

### Principios Arquitectónicos

El sistema está diseñado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una única razón para cambiar
    - Entidades: Solo contienen datos (DTOs)
    - Servicios: Solo contienen lógica de negocio
    - Patrones: Implementaciones aisladas y reutilizables

- **Open/Closed**: Abierto a extensión, cerrado a modificación
    - Nuevos tipos de propiedades: Agregar sin modificar factory existente
    - Nuevas estrategias de ajuste: Implementar interfaz sin cambiar servicios

- **Liskov Substitution**: Subtipos intercambiables
    - Todas las propiedades son Propiedad
    - Todas las estrategias implementan AjusteRentaStrategy

- **Interface Segregation**: Interfaces específicas
    - Observer[T]: Genérico para cualquier tipo de evento
    - AjusteRentaStrategy: Específico para ajustes de renta

- **Dependency Inversion**: Dependencias de abstracciones
    - Servicios dependen de Strategy (abstracción), no implementaciones
    - Factory retorna Propiedad (interfaz), no tipos concretos

### Separación de Capas

```
+----------------------------------+
|        PRESENTACIÓN              |
|  (main.py - Demostración CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (InmobiliariaService, Reporte)  |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (ContratoService, etc.)         |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Propiedad, Contrato, Persona)  |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

### Inyección de Dependencias

El sistema utiliza inyección manual de dependencias:

```python
# Estrategia inyectada en constructor
class ContratoService:
    def __init__(self):
        super().__init__(AjusteInflacionarioStrategy())

# Monitores inyectados en controlador
tarea_control = ControlVencimientoTask(
    tarea_fecha,      # Dependencia inyectada
    tarea_pago,       # Dependencia inyectada
    contrato,
    contrato_service
)
```

---

## Patrones de Diseño Implementados

### 1. SINGLETON Pattern

**Ubicación**: `python_inmobiliaria/servicios/propiedades/propiedad_service_registry.py`

**Problema que resuelve**:
- Garantizar una única instancia del registro de servicios
- Compartir estado entre todos los servicios del sistema
- Evitar múltiples registros inconsistentes

**Implementación**:
```python
class PropiedadServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Uso en el sistema**:
- Todos los servicios de propiedades comparten el mismo registry
- Elimina cadenas de `isinstance()` mediante dispatch polimórfico
- Acceso: `PropiedadServiceRegistry.get_instance()`

**Ventajas**:
- Thread-safe mediante Lock
- Inicialización perezosa (lazy initialization)
- Punto único de control

---

### 2. FACTORY METHOD Pattern

**Ubicación**: `python_inmobiliaria/patrones/factory/propiedad_factory.py`

**Problema que resuelve**:
- Creación de propiedades sin conocer clases concretas
- Encapsulación de lógica de construcción compleja
- Extensibilidad para nuevos tipos de propiedades

**Implementación**:
```python
class PropiedadFactory:
    @staticmethod
    def crear_propiedad(tipo: str) -> Propiedad:
        factories = {
            "Casa": PropiedadFactory._crear_casa,
            "Departamento": PropiedadFactory._crear_departamento,
            "Finca": PropiedadFactory._crear_finca
        }

        if tipo not in factories:
            raise ValueError(f"Tipo desconocido: {tipo}")

        return factories[tipo]()
```

**Uso en el sistema**:
```python
# InmobiliariaService usa factory internamente
inmobiliaria_service.registrar_propiedad("Casa", datos)
# Crea una Casa sin conocer constructor
```

**Ventajas**:
- Código cliente independiente de clases concretas
- Fácil agregar nuevos tipos de propiedades
- Validación centralizada de tipos

---

### 3. OBSERVER Pattern

**Ubicación**: `python_inmobiliaria/patrones/observer/`

**Problema que resuelve**:
- Notificación automática a múltiples observadores
- Desacoplamiento entre monitores y consumidores
- Sistema de eventos tipo-seguro

**Implementación**:
```python
class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso en el sistema**:
```python
# Monitor es Observable
class FechaMonitorTask(threading.Thread, Observable[date]):
    def run(self):
        while not self._detenido.is_set():
            fecha_actual = date.today()
            # Notifica a todos los observadores
            self.notificar_observadores(fecha_actual)
            time.sleep(INTERVALO_MONITOR_FECHA)

# ControlVencimientoTask es Observer
class ControlVencimientoTask(Observer[date]):
    def actualizar(self, evento: date) -> None:
        # Recibe notificación automáticamente
        self._fecha_actual = evento
```

**Ventajas**:
- Tipo-seguro con Generics
- Desacoplamiento total
- Múltiples observadores permitidos

---

### 4. STRATEGY Pattern

**Ubicación**: `python_inmobiliaria/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de ajuste intercambiables
- Eliminar condicionales tipo if/else
- Permitir cambios en tiempo de ejecución

**Implementación**:
```python
class AjusteRentaStrategy(ABC):
    @abstractmethod
    def calcular_ajuste(
        self,
        monto_actual: float,
        fecha_ajuste: date,
        contrato: 'Contrato'
    ) -> float:
        pass

# Estrategia 1: Inflacionario
class AjusteInflacionarioStrategy(AjusteRentaStrategy):
    def calcular_ajuste(self, monto_actual, fecha_ajuste, contrato):
        meses_transcurridos = self._calcular_meses(contrato.get_fecha_inicio(), fecha_ajuste)
        if meses_transcurridos >= 12:
            return monto_actual * AJUSTE_INFLACION_ANUAL  # 1.25
        else:
            return monto_actual

# Estrategia 2: Fijo
class AjusteFijoStrategy(AjusteRentaStrategy):
    def __init__(self, porcentaje: float):
        self._porcentaje = porcentaje

    def calcular_ajuste(self, monto_actual, fecha_ajuste, contrato):
        return monto_actual * (1 + self._porcentaje)
```

**Uso en el sistema**:
```python
# Inyección de estrategia en servicio
class ContratoService:
    def __init__(self):
        super().__init__(AjusteInflacionarioStrategy())

class ContratoFijoService:
    def __init__(self):
        super().__init__(AjusteFijoStrategy(0.10))  # 10% fijo
```

**Ventajas**:
- Algoritmos intercambiables
- Sin modificar código cliente
- Testeable independientemente

---

### 5. REGISTRY Pattern (Bonus)

**Ubicación**: `python_inmobiliaria/servicios/propiedades/propiedad_service_registry.py`

**Problema que resuelve**:
- Eliminar cascadas de `isinstance()`
- Dispatch polimórfico basado en tipo
- Punto único de registro de servicios

**Implementación**:
```python
class PropiedadServiceRegistry:
    def __init__(self):
        # Registro de handlers por tipo
        self._calcular_valor_handlers = {
            Casa: self._calcular_valor_casa,
            Departamento: self._calcular_valor_departamento,
            Finca: self._calcular_valor_finca
        }

    def calcular_valor(self, propiedad: Propiedad) -> float:
        tipo = type(propiedad)
        if tipo not in self._calcular_valor_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")

        # Dispatch polimórfico
        return self._calcular_valor_handlers[tipo](propiedad)
```

**Antes (con isinstance)**:
```python
if isinstance(propiedad, Casa):
    return casa_service.calcular_valor(propiedad)
elif isinstance(propiedad, Departamento):
    return departamento_service.calcular_valor(propiedad)
elif isinstance(propiedad, Finca):
    return finca_service.calcular_valor(propiedad)
# ... 3 más
```

**Después (con Registry)**:
```python
return registry.calcular_valor(propiedad)  # Despacho automático
```

---

## Requisitos del Sistema

### Requisitos de Software

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Módulos Estándar**: Solo biblioteca estándar de Python (sin dependencias externas)

### Requisitos de Hardware

- **RAM**: Mínimo 512 MB
- **Disco**: 50 MB libres
- **Procesador**: Cualquier procesador moderno (1 GHz+)

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/python-inmobiliaria.git
cd python-inmobiliaria
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Verificar Instalación

```bash
python --version
# Debe mostrar Python 3.13 o superior
```

### 4. Ejecutar Sistema

```bash
python main.py
```

**Salida esperada**:
```
======================================================================
      SISTEMA DE GESTIÓN DE ARRENDAMIENTOS Y CONTRATOS
======================================================================

----------------------------------------------------------------------
  PATRÓN SINGLETON: Inicializando servicios
----------------------------------------------------------------------
[OK] Todos los servicios comparten la misma instancia del Registry

1. Registrando propiedades...
...
======================================================================
              EJEMPLO COMPLETADO EXITOSAMENTE
======================================================================
  [OK] SINGLETON   - PropiedadServiceRegistry (instancia única)
  [OK] FACTORY     - Creación de propiedades
  [OK] OBSERVER    - Sistema de monitoreo y eventos
  [OK] STRATEGY    - Algoritmos de ajuste de renta
======================================================================
```

---

## Uso del Sistema

### Ejemplo Básico

```python
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService
from python_inmobiliaria.servicios.contratos.contrato_service import ContratoService

# 1. Registrar propiedad
propiedad_service = PropiedadService()
propiedad = propiedad_service.registrar_propiedad(
    tipo="Casa",
    direccion="Calle Falsa 123",
    superficie=150.0,
    propietario_dni=12345678
)

# 2. Crear inquilino
inquilino = Inquilino(
    dni=87654321,
    nombre="Juan Pérez",
    telefono="1234567890"
)

# 3. Crear contrato (usa Factory Method internamente)
contrato_service = ContratoService()
contrato = contrato_service.crear_contrato(
    propiedad=propiedad,
    inquilino=inquilino,
    monto_mensual=50000.0,
    fecha_inicio=date.today(),
    duracion_meses=12
)

# 4. Registrar pago (usa Strategy Pattern internamente)
contrato_service.registrar_pago(contrato, 50000.0, date.today())

# 5. Aplicar ajuste de renta
contrato_service.aplicar_ajuste(contrato)
```

### Sistema de Monitoreo Automatizado

```python
from python_inmobiliaria.monitoreo.monitores.fecha_monitor_task import FechaMonitorTask
from python_inmobiliaria.monitoreo.monitores.pago_monitor_task import PagoMonitorTask
from python_inmobiliaria.monitoreo.control.control_vencimiento_task import ControlVencimientoTask

# Crear monitores (Observable)
tarea_fecha = FechaMonitorTask()
tarea_pago = PagoMonitorTask()

# Crear controlador (Observer)
tarea_control = ControlVencimientoTask(
    tarea_fecha,
    tarea_pago,
    contrato,
    contrato_service
)

# Iniciar threads daemon
tarea_fecha.start()
tarea_pago.start()
tarea_control.start()

# Sistema funciona automáticamente
time.sleep(20)  # Dejarlo funcionar 20 segundos

# Detener sistema
tarea_fecha.detener()
tarea_pago.detener()
tarea_control.detener()
```

### Persistencia de Datos

```python
from python_inmobiliaria.servicios.registros.registro_inmobiliario_service import RegistroInmobiliarioService
from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

# Crear registro
registro = RegistroInmobiliario(
    id_registro=1,
    propiedad=propiedad,
    contrato=contrato,
    propietario="María González",
    valor_fiscal=5500000.00
)

# Persistir
registro_service = RegistroInmobiliarioService()
registro_service.persistir(registro)
# Crea archivo: data/Maria Gonzalez_Casa.dat

# Recuperar
registro_leido = RegistroInmobiliarioService.leer_registro("Maria Gonzalez", "Casa")
registro_service.mostrar_datos(registro_leido)
```

---

## Estructura del Proyecto

```
PythonInmobiliaria/
|
+-- main.py                          # Punto de entrada del sistema
+-- CLAUDE.md                        # Guía para Claude Code
+-- README.md                        # Este archivo
+-- USER_STORIES.md                  # Historias de usuario detalladas
+-- RUBRICA_EVALUACION.md            # Rúbrica de evaluación técnica
+-- RUBRICA_AUTOMATIZADA.md          # Rúbrica para automatización n8n
|
+-- .venv/                           # Entorno virtual Python
|
+-- data/                            # Datos persistidos (archivos .dat)
|
+-- python_inmobiliaria/             # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes centralizadas del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- __init__.py
    |   |
    |   +-- propiedades/             # Propiedades inmobiliarias
    |   |   +-- __init__.py
    |   |   +-- propiedad.py         # Interfaz base
    |   |   +-- inmueble.py          # Base para inmuebles
    |   |   +-- casa.py              # Propiedad tipo Casa
    |   |   +-- departamento.py      # Propiedad tipo Departamento
    |   |   +-- finca.py             # Propiedad tipo Finca
    |   |   +-- tipo_amenidad.py     # Enum de tipos de amenidades
    |   |
    |   +-- contratos/               # Gestión contractual
    |   |   +-- __init__.py
    |   |   +-- contrato.py          # Contrato de arrendamiento
    |   |   +-- pago.py              # Registro de pago
    |   |   +-- registro_inmobiliario.py # Registro completo
    |   |
    |   +-- personas/                # Gestión de personas
    |       +-- __init__.py
    |       +-- inquilino.py         # Inquilino arrendatario
    |       +-- propietario.py       # Propietario de inmuebles
    |       +-- garantia.py          # Garantía de alquiler
    |       +-- referencia.py        # Referencia personal
    |
    +-- servicios/                   # Lógica de negocio
    |   +-- __init__.py
    |   |
    |   +-- propiedades/             # Servicios de propiedades
    |   |   +-- __init__.py
    |   |   +-- propiedad_service.py              # Servicio base
    |   |   +-- inmueble_service.py               # Servicio base inmuebles
    |   |   +-- casa_service.py                   # Servicio Casa
    |   |   +-- departamento_service.py           # Servicio Departamento
    |   |   +-- finca_service.py                  # Servicio Finca
    |   |   +-- propiedad_service_registry.py     # Registry + Singleton
    |   |
    |   +-- contratos/               # Servicios contractuales
    |   |   +-- __init__.py
    |   |   +-- contrato_service.py               # Servicio Contrato
    |   |   +-- pago_service.py                   # Servicio Pago
    |   |   +-- registro_inmobiliario_service.py  # Servicio Registro
    |   |
    |   +-- personas/                # Servicios de personas
    |   |   +-- __init__.py
    |   |   +-- inquilino_service.py              # Servicio Inquilino
    |   |
    |   +-- negocio/                 # Servicios de alto nivel
    |       +-- __init__.py
    |       +-- inmobiliaria_service.py           # Operaciones inmobiliarias
    |       +-- reporte.py                        # Reportes genéricos
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- __init__.py
    |   |
    |   +-- singleton/               # Patrón Singleton
    |   |   +-- __init__.py
    |   |
    |   +-- factory/                 # Patrón Factory Method
    |   |   +-- __init__.py
    |   |   +-- propiedad_factory.py              # Factory de propiedades
    |   |
    |   +-- observer/                # Patrón Observer
    |   |   +-- __init__.py
    |   |   +-- observable.py                     # Clase Observable[T]
    |   |   +-- observer.py                       # Interfaz Observer[T]
    |   |   +-- eventos/
    |   |       +-- __init__.py
    |   |       +-- evento_monitor.py             # Evento de monitores
    |   |       +-- evento_contrato.py            # Evento de contrato
    |   |
    |   +-- strategy/                # Patrón Strategy
    |       +-- __init__.py
    |       +-- ajuste_renta_strategy.py          # Interfaz Strategy
    |       +-- impl/
    |           +-- __init__.py
    |           +-- ajuste_inflacionario_strategy.py      # Inflacionario
    |           +-- ajuste_fijo_strategy.py               # Fijo
    |
    +-- monitoreo/                   # Sistema de monitoreo automatizado
    |   +-- __init__.py
    |   |
    |   +-- monitores/               # Monitores de eventos
    |   |   +-- __init__.py
    |   |   +-- fecha_monitor_task.py             # Monitor de fechas
    |   |   +-- pago_monitor_task.py              # Monitor de pagos
    |   |
    |   +-- control/                 # Control de vencimientos
    |       +-- __init__.py
    |       +-- control_vencimiento_task.py       # Controlador
    |
    +-- excepciones/                 # Excepciones personalizadas
        +-- __init__.py
        +-- inmobiliaria_exception.py             # Excepción base
        +-- contrato_vencido_exception.py
        +-- pago_insuficiente_exception.py
        +-- persistencia_exception.py
        +-- mensajes_exception.py                 # Mensajes centralizados
```

---

## Módulos del Sistema

### Módulo: `entidades`

**Responsabilidad**: Objetos de dominio puros (DTOs - Data Transfer Objects)

**Características**:
- Solo contienen datos y getters/setters
- NO contienen lógica de negocio
- Campos privados con encapsulación

**Clases principales**:
- `Propiedad`: Interfaz base para todas las propiedades
- `Inmueble`: Base para propiedades edificadas (Casa, Departamento)
- `Casa`: Propiedad unifamiliar
- `Departamento`: Unidad en edificio
- `Finca`: Propiedad rural
- `Contrato`: Contrato de arrendamiento
- `Inquilino`: Persona arrendataria

---

### Módulo: `servicios`

**Responsabilidad**: Lógica de negocio del sistema

**Características**:
- Servicios sin estado (stateless)
- Operaciones sobre entidades
- Orquestación de patrones

**Servicios principales**:
- `ContratoService`: Crear, renovar, aplicar ajustes
- `InquilinoService`: Asignar contratos, verificar garantías
- `RegistroInmobiliarioService`: Persistir y recuperar registros
- `InmobiliariaService`: Operaciones de alto nivel

---

### Módulo: `patrones`

**Responsabilidad**: Implementaciones de patrones de diseño

**Patrones incluidos**:
1. **Singleton**: `PropiedadServiceRegistry`
2. **Factory Method**: `PropiedadFactory`
3. **Observer**: `Observable[T]` / `Observer[T]`
4. **Strategy**: `AjusteRentaStrategy` + implementaciones

---

### Módulo: `monitoreo`

**Responsabilidad**: Sistema de monitoreo automatizado con threads

**Componentes**:
- **Monitores** (Observable):
    - `FechaMonitorTask`: Monitorea fecha actual cada día
    - `PagoMonitorTask`: Monitorea pagos pendientes cada hora

- **Control** (Observer):
    - `ControlVencimientoTask`: Observa monitores y genera alertas

**Modelo de threading**:
- Threads daemon (finalizan con main)
- Graceful shutdown con `threading.Event`
- Timeouts configurables

---

### Módulo: `excepciones`

**Responsabilidad**: Excepciones de dominio específicas

**Jerarquía**:
```
InmobiliariaException (base)
  +-- ContratoVencidoException
  +-- PagoInsuficienteException
  +-- PersistenciaException
```

**Características**:
- Mensajes separados: usuario vs técnico
- Contexto específico del error
- Causas encadenadas

---

## Documentación Técnica

### Convenciones de Código

#### PEP 8 Compliance (100%)

- **Nombres de variables**: `snake_case`
- **Nombres de clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE` en `constantes.py`
- **Privados**: Prefijo `_nombre`

#### Docstrings (Google Style)

```python
def metodo(self, parametro: str) -> int:
    """
    Descripción breve del método.

    Args:
        parametro: Descripción del parámetro

    Returns:
        Descripción del valor de retorno

    Raises:
        ValueError: Cuando ocurre validación
    """
```

#### Type Hints

```python
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from modulo import Clase  # Evita imports circulares

def metodo(self, lista: List[int]) -> Optional[str]:
    pass
```

### Configuración de Constantes

Todas las constantes en `constantes.py`:

```python
# Contratos
DURACION_MINIMA_MESES = 6
DURACION_MAXIMA_MESES = 36
DEPOSITO_GARANTIA_MESES = 2

# Ajustes
AJUSTE_INFLACION_ANUAL = 1.25
MESES_AJUSTE_CONTRATO = 12

# Monitoreo
INTERVALO_MONITOR_FECHA = 86400  # 1 día en segundos
INTERVALO_MONITOR_PAGO = 3600    # 1 hora en segundos
DIAS_ALERTA_VENCIMIENTO = 30
```

**Regla**: NUNCA hardcodear valores mágicos en el código.

### Manejo de Excepciones

```python
try:
    contrato_service.crear_contrato(propiedad, inquilino, monto, fecha, duracion)
except ContratoVencidoException as e:
    print(e.get_user_message())
    print(f"Fecha vencimiento: {e.get_fecha_vencimiento()}")
    print(f"Fecha actual: {e.get_fecha_actual()}")
except InmobiliariaException as e:
    print(e.get_full_message())
```

---

## Testing y Validación

### Ejecución del Sistema Completo

El archivo `main.py` contiene un test de integración completo que valida:

1. [x] Patrón Singleton - Instancia única compartida
2. [x] Patrón Factory - Creación de 3 tipos de propiedades
3. [x] Patrón Observer - Monitores y notificaciones
4. [x] Patrón Strategy - Ajuste diferenciado
5. [x] Registro de propiedades y contratos
6. [x] Monitoreo automatizado
7. [x] Gestión de inquilinos con garantías
8. [x] Pagos y reportes
9. [x] Persistencia y recuperación
10. [x] Threading y graceful shutdown

### Validación Manual

```bash
python main.py
```

**Criterios de éxito**:
- No errores de importación
- No excepciones no controladas
- Mensaje final: `EJEMPLO COMPLETADO EXITOSAMENTE`
- Archivo creado: `data/Maria Gonzalez_Casa.dat`

### Casos de Prueba

#### Caso 1: Contrato Vencido
```python
# Contrato con fecha de vencimiento pasada
try:
    contrato_service.renovar_contrato(contrato_vencido)
except ContratoVencidoException as e:
    assert e.get_fecha_vencimiento() < date.today()
```

#### Caso 2: Pago Insuficiente
```python
# Pago menor al monto requerido
contrato.set_monto_mensual(50000.0)
try:
    pago_service.registrar_pago(contrato, 30000.0)
except PagoInsuficienteException as e:
    assert "insuficiente" in e.get_user_message().lower()
```

#### Caso 3: Inquilino Sin Garantía
```python
# Inquilino sin garantía no puede firmar contrato
inquilino = Inquilino(12345678, "Test", "1234567890")
resultado = inquilino_service.verificar_garantia(inquilino)
assert resultado == False
```

---

## Contribución

### Cómo Agregar un Nuevo Tipo de Propiedad

#### Paso 1: Definir Constantes

En `constantes.py`:
```python
# Constantes del nuevo tipo
SUPERFICIE_LOCAL = 80.0
VALOR_BASE_LOCAL = 3000000.0
```

#### Paso 2: Crear Entidad

En `entidades/propiedades/local.py`:
```python
from python_inmobiliaria.entidades.propiedades.inmueble import Inmueble
from python_inmobiliaria.constantes import (
    VALOR_BASE_LOCAL,
    SUPERFICIE_LOCAL
)

class Local(Inmueble):
    """Entidad Local Comercial - solo datos."""

    def __init__(self, tipo_comercio: str):
        super().__init__(
            valor_base=VALOR_BASE_LOCAL,
            superficie=SUPERFICIE_LOCAL
        )
        self._tipo_comercio = tipo_comercio

    def get_tipo_comercio(self) -> str:
        return self._tipo_comercio

    def set_tipo_comercio(self, tipo_comercio: str) -> None:
        self._tipo_comercio = tipo_comercio
```

#### Paso 3: Crear Servicio

En `servicios/propiedades/local_service.py`:
```python
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService
from python_inmobiliaria.patrones.strategy.impl.ajuste_fijo_strategy import AjusteFijoStrategy

class LocalService(PropiedadService):
    """Servicio para Local."""

    def __init__(self):
        super().__init__(AjusteFijoStrategy(0.15))

    def mostrar_datos(self, propiedad: 'Local') -> None:
        super().mostrar_datos(propiedad)
        print(f"Tipo de comercio: {propiedad.get_tipo_comercio()}")
```

#### Paso 4: Registrar en Registry

En `propiedad_service_registry.py`:
```python
from python_inmobiliaria.entidades.propiedades.local import Local
from python_inmobiliaria.servicios.propiedades.local_service import LocalService

class PropiedadServiceRegistry:
    def __init__(self):
        self._local_service = LocalService()

        self._calcular_valor_handlers[Local] = self._calcular_valor_local
        self._mostrar_datos_handlers[Local] = self._mostrar_datos_local

    def _calcular_valor_local(self, propiedad):
        return self._local_service.calcular_valor(propiedad)

    def _mostrar_datos_local(self, propiedad):
        return self._local_service.mostrar_datos(propiedad)
```

#### Paso 5: Registrar en Factory

En `propiedad_factory.py`:
```python
@staticmethod
def _crear_local() -> Local:
    from python_inmobiliaria.entidades.propiedades.local import Local
    return Local(tipo_comercio="Oficina")

@staticmethod
def crear_propiedad(tipo: str) -> Propiedad:
    factories = {
        # ... existentes
        "Local": PropiedadFactory._crear_local
    }
```

#### Paso 6: Usar el Nuevo Tipo

```python
inmobiliaria_service.registrar_propiedad("Local", datos)
```

---

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## Contacto y Soporte

- **Documentación**: Ver `CLAUDE.md` para guía técnica detallada
- **Historias de Usuario**: Ver `USER_STORIES.md` para casos de uso
- **Rúbrica de Evaluación**: Ver `RUBRICA_EVALUACION.md`

---

## Notas Adicionales

### Compatibilidad con Windows

El sistema fue desarrollado y probado en Windows. Consideraciones:

- **NO usar emojis** en print (problema de encoding)
- **NO usar caracteres Unicode especiales** en consola
- Usar solo ASCII estándar: `[OK]`, `[!]`, `[INFO]`

### Rendimiento

- Sistema optimizado para operaciones locales
- Threads livianos para monitores
- Persistencia con Pickle (rápida pero NO para producción)

### Limitaciones Conocidas

1. Pickle NO es seguro para datos no confiables
2. Sistema single-process (no distribuido)
3. Sin base de datos relacional
4. Sin interfaz gráfica (solo CLI)

**Este es un proyecto EDUCATIVO** enfocado en patrones de diseño, NO en producción real.

---

**Última actualización**: Noviembre 2025
**Versión del sistema**: 1.0.0
**Python requerido**: 3.13+