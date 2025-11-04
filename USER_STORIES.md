# Historias de Usuario - Sistema de Gestión de Arrendamientos y Contratos

**Proyecto**: PythonInmobiliaria
**Versión**: 1.0.0
**Fecha**: Noviembre 2025
**Metodología**: User Story Mapping

---

## Índice

1. [Epic 1: Gestión de Propiedades y Contratos](#epic-1-gestión-de-propiedades-y-contratos)
2. [Epic 2: Gestión de Propiedades Inmobiliarias](#epic-2-gestión-de-propiedades-inmobiliarias)
3. [Epic 3: Sistema de Monitoreo Automatizado](#epic-3-sistema-de-monitoreo-automatizado)
4. [Epic 4: Gestión de Personas](#epic-4-gestión-de-personas)
5. [Epic 5: Operaciones de Negocio](#epic-5-operaciones-de-negocio)
6. [Epic 6: Persistencia y Auditoría](#epic-6-persistencia-y-auditoría)
7. [Historias Técnicas (Patrones de Diseño)](#historias-técnicas-patrones-de-diseño)

---

## Epic 1: Gestión de Propiedades y Contratos

### US-001: Registrar Propiedad Inmobiliaria

**Como** administrador inmobiliario
**Quiero** registrar una propiedad con sus datos catastrales y características
**Para** tener un control oficial de los inmuebles gestionados

#### Criterios de Aceptación

- [x] El sistema debe permitir crear una propiedad con:
    - Dirección completa (calle, número, ciudad)
    - Superficie en metros cuadrados (número positivo)
    - DNI del propietario (número entero positivo)
    - Valor fiscal estimado
- [x] La superficie debe ser mayor a 0, si no lanzar `ValueError`
- [x] La propiedad debe poder modificarse posteriormente
- [x] El sistema debe validar que los datos sean consistentes

#### Detalles Técnicos

**Clase**: `Propiedad` (`python_inmobiliaria/entidades/propiedades/propiedad.py`)
**Servicio**: `PropiedadService` (`python_inmobiliaria/servicios/propiedades/propiedad_service.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService

propiedad_service = PropiedadService()
propiedad = propiedad_service.registrar_propiedad(
    tipo="Casa",
    direccion="Av. San Martín 1500",
    superficie=150.0,
    propietario_dni=12345678
)
```

**Validaciones**:
```python
# Superficie válida
propiedad.set_superficie(180.0)  # OK

# Superficie inválida
propiedad.set_superficie(-50.0)  # ValueError: superficie debe ser mayor a cero
propiedad.set_superficie(0)  # ValueError: superficie debe ser mayor a cero
```

**Trazabilidad**: `main.py` líneas 111-116

---

### US-002: Crear Contrato de Arrendamiento

**Como** administrador de inmobiliaria
**Quiero** crear un contrato vinculando inquilino y propiedad
**Para** formalizar la relación de arrendamiento

#### Criterios de Aceptación

- [x] Un contrato debe tener:
    - Número único de contrato
    - Fecha de inicio y vencimiento
    - Monto mensual del alquiler
    - Inquilino asociado
    - Propiedad arrendada
- [x] El contrato debe estar asociado a una propiedad disponible
- [x] El monto mensual no puede ser negativo
- [x] El sistema debe controlar fechas de vencimiento

#### Detalles Técnicos

**Clase**: `Contrato` (`python_inmobiliaria/entidades/contratos/contrato.py`)
**Servicio**: `ContratoService` (`python_inmobiliaria/servicios/contratos/contrato_service.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.entidades.contratos.contrato import Contrato
from datetime import date, timedelta

contrato = Contrato(
    numero_contrato=1,
    fecha_inicio=date.today(),
    fecha_vencimiento=date.today() + timedelta(days=365),
    monto_mensual=50000.0,
    inquilino=inquilino,
    propiedad=propiedad
)
```

**Validaciones**:
```python
# Monto válido
contrato.set_monto_mensual(55000.0)  # OK

# Monto inválido
contrato.set_monto_mensual(-1000.0)  # ValueError: monto no puede ser negativo
```

**Trazabilidad**: `main.py` línea 117, `contrato_service.py` líneas 21-54

---

### US-003: Crear Registro Inmobiliario Completo

**Como** auditor contable
**Quiero** crear un registro inmobiliario que vincule propiedad, contrato, propietario y valor fiscal
**Para** tener documentación oficial completa

#### Criterios de Aceptación

- [x] Un registro inmobiliario debe contener:
    - ID de registro (número único)
    - Referencia a Propiedad
    - Referencia a Contrato
    - Nombre del propietario
    - Valor fiscal (número decimal positivo)
- [x] Todos los campos son obligatorios
- [x] El registro debe poder persistirse y recuperarse
- [x] El registro debe poder mostrarse en consola con formato

#### Detalles Técnicos

**Clase**: `RegistroInmobiliario` (`python_inmobiliaria/entidades/registros/registro_inmobiliario.py`)
**Servicio**: `RegistroInmobiliarioService` (`python_inmobiliaria/servicios/registros/registro_inmobiliario_service.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

registro = RegistroInmobiliario(
    id_registro=1,
    propiedad=propiedad,
    contrato=contrato,
    propietario="María González",
    valor_fiscal=5500000.00
)
```

**Salida de mostración**:
```
REGISTRO INMOBILIARIO
=====================
ID Registro:  1
Propietario:  María González
Valor Fiscal: 5500000.00
Dirección:    Av. San Martín 1500
Superficie:   150.0 m²
Contrato activo: Sí
Monto mensual: $50000.00
```

**Trazabilidad**: `main.py` líneas 123-129

---

## Epic 2: Gestión de Propiedades Inmobiliarias

### US-004: Registrar Casas

**Como** administrador inmobiliario
**Quiero** registrar casas con características específicas
**Para** gestionar propiedades unifamiliares

#### Criterios de Aceptación

- [x] Debe poder registrar múltiples casas
- [x] Cada casa debe tener:
    - Dirección completa
    - Superficie total en m²
    - Metros de terreno
    - Cantidad de plantas
    - Garaje (sí/no)
- [x] El sistema debe calcular valor estimado
- [x] Las casas deben crearse vía Factory Method (no instanciación directa)

#### Detalles Técnicos

**Clase**: `Casa` (`python_inmobiliaria/entidades/propiedades/casa.py`)
**Servicio**: `CasaService` (`python_inmobiliaria/servicios/propiedades/casa_service.py`)
**Factory**: `PropiedadFactory` (`python_inmobiliaria/patrones/factory/propiedad_factory.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.propiedades.propiedad_service import PropiedadService

propiedad_service = PropiedadService()

# Registrar casa (usa Factory Method internamente)
casa = propiedad_service.registrar_propiedad(
    tipo="Casa",
    direccion="Calle Los Robles 456",
    superficie=180.0,
    propietario_dni=23456789
)
```

**Constantes utilizadas**:
```python
SUPERFICIE_MINIMA_CASA = 50.0  # m²
VALOR_BASE_CASA = 4000000.0  # pesos
FACTOR_TERRENO = 1.2
```

**Trazabilidad**: `main.py` línea 141

---

### US-005: Registrar Departamentos

**Como** administrador inmobiliario
**Quiero** registrar departamentos especificando piso y amenidades
**Para** gestionar unidades en edificios

#### Criterios de Aceptación

- [x] Debe poder registrar múltiples departamentos
- [x] Cada departamento debe tener:
    - Dirección del edificio
    - Número de piso
    - Número de departamento
    - Superficie en m²
    - Amenidades (piscina, gimnasio, seguridad)
- [x] El sistema debe calcular valor según piso
- [x] Los departamentos deben crearse vía Factory Method

#### Detalles Técnicos

**Clase**: `Departamento` (`python_inmobiliaria/entidades/propiedades/departamento.py`)
**Enum**: `TipoAmenidad` (`python_inmobiliaria/entidades/propiedades/tipo_amenidad.py`)
**Servicio**: `DepartamentoService` (`python_inmobiliaria/servicios/propiedades/departamento_service.py`)

**Código de ejemplo**:
```python
# Registrar departamento
departamento = propiedad_service.registrar_propiedad(
    tipo="Departamento",
    direccion="Torre Mirador - Piso 8 - Depto 2",
    superficie=75.0,
    propietario_dni=34567890
)
```

**Tipos de amenidades disponibles**:
```python
from python_inmobiliaria.entidades.propiedades.tipo_amenidad import TipoAmenidad

TipoAmenidad.PISCINA
TipoAmenidad.GIMNASIO
TipoAmenidad.SEGURIDAD
TipoAmenidad.SALON_EVENTOS
```

**Constantes utilizadas**:
```python
SUPERFICIE_MINIMA_DEPTO = 30.0  # m²
VALOR_BASE_DEPTO = 2500000.0  # pesos
FACTOR_PISO = 0.05  # 5% adicional por piso
```

**Trazabilidad**: `main.py` línea 142

---

### US-006: Registrar Fincas

**Como** administrador inmobiliario
**Quiero** registrar fincas rurales con extensión y características
**Para** gestionar propiedades de gran superficie

#### Criterios de Aceptación

- [x] Debe poder registrar múltiples fincas
- [x] Cada finca debe tener:
    - Ubicación (paraje, ruta)
    - Extensión en hectáreas
    - Tipo de suelo (productivo, árido, mixto)
    - Acceso a agua (sí/no)
    - Construcciones existentes
- [x] El sistema debe calcular valor por hectárea
- [x] Las fincas ocupan mayor superficie que otros tipos

#### Detalles Técnicos

**Clase**: `Finca` (`python_inmobiliaria/entidades/propiedades/finca.py`)
**Servicio**: `FincaService` (`python_inmobiliaria/servicios/propiedades/finca_service.py`)

**Código de ejemplo**:
```python
# Registrar finca
finca = propiedad_service.registrar_propiedad(
    tipo="Finca",
    direccion="Ruta 40 Km 1250 - Uspallata",
    superficie=50000.0,  # 5 hectáreas
    propietario_dni=45678901
)
```

**Constantes utilizadas**:
```python
SUPERFICIE_MINIMA_FINCA = 10000.0  # m² (1 hectárea)
VALOR_BASE_HECTAREA = 800000.0  # pesos
```

**Trazabilidad**: `main.py` línea 143

---

### US-007: Calcular Valor de Propiedades

**Como** administrador inmobiliario
**Quiero** calcular el valor estimado de cada propiedad
**Para** establecer precios de alquiler justos

#### Criterios de Aceptación

- [x] El sistema debe calcular valores diferenciados por tipo
- [x] Debe considerar:
    - **Casa**: Superficie, terreno, ubicación
    - **Departamento**: Superficie, piso, amenidades
    - **Finca**: Extensión, productividad, accesos
- [x] Usar el patrón Registry para dispatch polimórfico
- [x] NO usar cascadas de isinstance()

#### Detalles Técnicos

**Registry**: `PropiedadServiceRegistry.calcular_valor()`

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.propiedades.propiedad_service_registry import PropiedadServiceRegistry

registry = PropiedadServiceRegistry.get_instance()

for propiedad in propiedades:
    valor = registry.calcular_valor(propiedad)
    print(f"Valor estimado: ${valor:,.2f}")
```

**Salida ejemplo (Casa)**:
```
Propiedad: Casa
Dirección: Calle Los Robles 456
Superficie: 180.0 m²
Valor estimado: $7,200,000.00
```

**Trazabilidad**: `propiedad_service_registry.py` líneas 78-89

---

### US-008: Registrar Pagos de Alquiler

**Como** administrador inmobiliario
**Quiero** registrar pagos de alquileres recibidos
**Para** mantener control financiero actualizado

#### Criterios de Aceptación

- [x] El registro de pago debe:
    - Asociarse a un contrato específico
    - Registrar fecha de pago
    - Registrar monto abonado
    - Validar que el monto coincida con lo adeudado
- [x] Si el monto es insuficiente, lanzar `PagoInsuficienteException`
- [x] Los pagos deben actualizar el estado del contrato
- [x] El sistema debe usar el patrón Strategy para cálculos

#### Detalles Técnicos

**Servicio**: `PagoService.registrar_pago()`
**Estrategias**:
- `AjusteInflacionarioStrategy` (contratos anuales)
- `AjusteFijoStrategy` (contratos con ajuste pactado)

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.contratos.pago_service import PagoService

pago_service = PagoService()

# Registrar pago
pago_service.registrar_pago(
    contrato=contrato,
    monto=50000.0,
    fecha_pago=date.today()
)
```

**Validaciones**:
```python
# Pago correcto
pago_service.registrar_pago(contrato, 50000.0, date.today())  # OK

# Pago insuficiente
try:
    pago_service.registrar_pago(contrato, 30000.0, date.today())
except PagoInsuficienteException as e:
    print(f"Error: {e.get_user_message()}")
```

**Trazabilidad**: `pago_service.py` líneas 82-129

---

### US-009: Mostrar Datos de Propiedades por Tipo

**Como** administrador inmobiliario
**Quiero** ver los datos de cada propiedad de forma específica
**Para** conocer el estado actual del portafolio

#### Criterios de Aceptación

- [x] El sistema debe mostrar datos específicos por tipo:
    - **Casa**: Dirección, Superficie, Terreno, Plantas, Garaje, Valor
    - **Departamento**: Dirección, Superficie, Piso, Número, Amenidades, Valor
    - **Finca**: Ubicación, Extensión, Tipo suelo, Agua, Valor
- [x] Usar el patrón Registry para dispatch polimórfico
- [x] NO usar cascadas de isinstance()

#### Detalles Técnicos

**Registry**: `PropiedadServiceRegistry.mostrar_datos()`

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.propiedades.propiedad_service_registry import PropiedadServiceRegistry

registry = PropiedadServiceRegistry.get_instance()

for propiedad in propiedades:
    registry.mostrar_datos(propiedad)
    # Despacho automático al servicio correcto
```

**Salida ejemplo (Casa)**:
```
Propiedad: Casa
Dirección: Calle Los Robles 456
Superficie: 180.0 m²
Terreno: 250.0 m²
Plantas: 2
Garaje: Sí
Valor estimado: $7,200,000.00
```

**Trazabilidad**: `propiedad_service_registry.py` líneas 78-89

---

## Epic 3: Sistema de Monitoreo Automatizado

### US-010: Monitorear Fechas en Tiempo Real

**Como** sistema de gestión automatizado
**Quiero** monitorear la fecha actual continuamente
**Para** detectar vencimientos de contratos y pagos

#### Criterios de Aceptación

- [x] El monitor debe:
    - Ejecutarse en un thread daemon separado
    - Verificar fecha actual cada 24 horas (configurable)
    - Notificar a observadores cada verificación
    - Soportar detención graceful con timeout
- [x] Implementar patrón Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[date]`

#### Detalles Técnicos

**Clase**: `FechaMonitorTask` (`python_inmobiliaria/monitoreo/monitores/fecha_monitor_task.py`)
**Patrón**: Observer (Observable[date])

**Código de ejemplo**:
```python
from python_inmobiliaria.monitoreo.monitores.fecha_monitor_task import FechaMonitorTask

# Crear monitor (thread daemon)
tarea_fecha = FechaMonitorTask()

# Iniciar monitoreo continuo
tarea_fecha.start()

# Detener cuando sea necesario
tarea_fecha.detener()
tarea_fecha.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_MONITOR_FECHA = 86400  # segundos (1 día)
```

**Eventos generados**:
```python
# Cada verificación notifica fecha actual a observadores
fecha_actual: date = date.today()
self.notificar_observadores(fecha_actual)
```

**Trazabilidad**: `main.py` líneas 158-166

---

### US-011: Monitorear Pagos Pendientes

**Como** sistema de gestión automatizado
**Quiero** monitorear pagos pendientes continuamente
**Para** generar alertas de morosidad

#### Criterios de Aceptación

- [x] El monitor debe:
    - Ejecutarse en un thread daemon separado
    - Verificar pagos pendientes cada hora (configurable)
    - Notificar a observadores cada verificación
    - Soportar detención graceful con timeout
- [x] Implementar patrón Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[List[Contrato]]`

#### Detalles Técnicos

**Clase**: `PagoMonitorTask` (`python_inmobiliaria/monitoreo/monitores/pago_monitor_task.py`)
**Patrón**: Observer (Observable[List[Contrato]])

**Código de ejemplo**:
```python
from python_inmobiliaria.monitoreo.monitores.pago_monitor_task import PagoMonitorTask

# Crear monitor (thread daemon)
tarea_pago = PagoMonitorTask()

# Iniciar monitoreo continuo
tarea_pago.start()

# Detener cuando sea necesario
tarea_pago.detener()
tarea_pago.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_MONITOR_PAGO = 3600  # segundos (1 hora)
```

**Trazabilidad**: `main.py` líneas 158-166

---

### US-012: Control Automático de Vencimientos

**Como** sistema de gestión automatizado
**Quiero** generar alertas automáticas de vencimientos próximos
**Para** notificar con anticipación a propietarios e inquilinos

#### Criterios de Aceptación

- [x] El controlador debe:
    - Ejecutarse en un thread daemon separado
    - Evaluar vencimientos cada día
    - Observar monitores de fecha y pagos
    - Generar alertas cuando:
        - Días para vencimiento <= 30, O
        - Pagos atrasados > 0
    - NO generar alertas si todo está en orden
- [x] Implementar patrón Observer (Observer[date])
- [x] Recibir monitores vía inyección de dependencias

#### Detalles Técnicos

**Clase**: `ControlVencimientoTask` (`python_inmobiliaria/monitoreo/control/control_vencimiento_task.py`)
**Patrón**: Observer (observa monitores)

**Código de ejemplo**:
```python
from python_inmobiliaria.monitoreo.control.control_vencimiento_task import ControlVencimientoTask

# Inyectar dependencias
tarea_control = ControlVencimientoTask(
    monitor_fecha=tarea_fecha,
    monitor_pago=tarea_pago,
    contrato=contrato,
    contrato_service=contrato_service
)

# Iniciar control automático
tarea_control.start()

# Detener cuando sea necesario
tarea_control.detener()
tarea_control.join(timeout=2.0)
```

**Lógica de decisión**:
```python
dias_vencimiento = (contrato.get_fecha_vencimiento() - fecha_actual).days

if dias_vencimiento <= DIAS_ALERTA_VENCIMIENTO:
    # GENERAR ALERTA
    self._generar_alerta_vencimiento(contrato)
elif contrato.tiene_pagos_atrasados():
    # GENERAR ALERTA MOROSIDAD
    self._generar_alerta_morosidad(contrato)
else:
    # TODO EN ORDEN
    pass
```

**Constantes de control**:
```python
DIAS_ALERTA_VENCIMIENTO = 30  # días
INTERVALO_CONTROL_VENCIMIENTO = 86400  # segundos (1 día)
```

**Trazabilidad**: `main.py` líneas 160-166, `control_vencimiento_task.py` líneas 67-91

---

### US-013: Detener Sistema de Monitoreo de Forma Segura

**Como** administrador del sistema
**Quiero** detener el sistema de monitoreo de forma controlada
**Para** evitar corrupción de datos o procesos incompletos

#### Criterios de Aceptación

- [x] El sistema debe:
    - Detener todos los threads con `threading.Event`
    - Esperar finalización con timeout configurable (2s)
    - NO forzar terminación abrupta
    - Permitir que threads completen operación actual
- [x] Threads deben ser daemon (finalizan con main)
- [x] Usar timeout de `constantes.py`

#### Detalles Técnicos

**Código de ejemplo**:
```python
from python_inmobiliaria.constantes import THREAD_JOIN_TIMEOUT

# Detener monitores y control
tarea_fecha.detener()
tarea_pago.detener()
tarea_control.detener()

# Esperar finalización con timeout
tarea_fecha.join(timeout=THREAD_JOIN_TIMEOUT)  # 2s
tarea_pago.join(timeout=THREAD_JOIN_TIMEOUT)
tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

# Si timeout expira, threads daemon finalizan automáticamente
```

**Constantes**:
```python
THREAD_JOIN_TIMEOUT = 2.0  # segundos
```

**Trazabilidad**: `main.py` líneas 256-263

---

## Epic 4: Gestión de Personas

### US-014: Registrar Inquilino con Referencias

**Como** administrador inmobiliario
**Quiero** registrar inquilinos con sus referencias personales
**Para** evaluar la confiabilidad del arrendatario

#### Criterios de Aceptación

- [x] Un inquilino debe tener:
    - DNI único (número entero)
    - Nombre completo
    - Teléfono de contacto
    - Lista de referencias personales (puede estar vacía)
    - Garantía de alquiler (inicialmente sin garantía)
- [x] Las referencias deben tener:
    - Nombre del referente
    - Teléfono de contacto
    - Relación con el inquilino
- [x] Un inquilino puede tener múltiples referencias
- [x] Lista de referencias es inmutable (defensive copy)

#### Detalles Técnicos

**Clases**:
- `Inquilino` (`python_inmobiliaria/entidades/personas/inquilino.py`)
- `Referencia` (`python_inmobiliaria/entidades/personas/referencia.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.entidades.personas.inquilino import Inquilino
from python_inmobiliaria.entidades.personas.referencia import Referencia

# Crear referencias
referencias = [
    Referencia("Carlos López", "261-4567890", "Laboral"),
    Referencia("Ana Martínez", "261-7891234", "Personal"),
    Referencia("Pedro Gómez", "261-1234567", "Familiar")
]

# Crear inquilino
inquilino = Inquilino(
    dni=43888734,
    nombre="Juan Pérez",
    telefono="261-9876543",
    referencias=referencias
)
```

**Trazabilidad**: `main.py` líneas 176-185

---

### US-015: Asignar Garantía a Inquilino

**Como** administrador inmobiliario
**Quiero** asignar una garantía de alquiler a un inquilino
**Para** asegurar el cumplimiento del contrato

#### Criterios de Aceptación

- [x] Una garantía debe tener:
    - Tipo (depósito, aval, seguro de caución)
    - Monto del depósito
    - Fecha de constitución
    - Estado (activa/devuelta)
- [x] El sistema debe verificar garantía antes de firmar contrato
- [x] Si no tiene garantía válida, no puede firmar contrato
- [x] El servicio debe permitir asignar/actualizar garantía

#### Detalles Técnicos

**Clase**: `Garantia` (`python_inmobiliaria/entidades/personas/garantia.py`)
**Servicio**: `InquilinoService.asignar_garantia()`

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.personas.inquilino_service import InquilinoService
from datetime import date

inquilino_service = InquilinoService()

# Asignar garantía
inquilino_service.asignar_garantia(
    inquilino=inquilino,
    tipo="Depósito",
    monto=100000.0,
    fecha_constitucion=date.today()
)

# Verificar garantía
if inquilino.get_garantia().esta_activa():
    print("Inquilino tiene garantía activa")
else:
    print("Inquilino NO tiene garantía")
```

**Trazabilidad**: `main.py` líneas 191-196

---

### US-016: Firmar Contrato de Arrendamiento

**Como** inquilino
**Quiero** firmar un contrato de arrendamiento
**Para** formalizar mi alquiler

#### Criterios de Aceptación

- [x] El inquilino debe:
    - Tener garantía válida
    - Aceptar términos del contrato
    - Proporcionar documentación requerida
- [x] El contrato debe registrarse en el sistema
- [x] Si no tiene garantía, retornar False (no puede firmar)
- [x] Si tiene garantía, retornar True (puede firmar)

#### Detalles Técnicos

**Servicio**: `InquilinoService.firmar_contrato()`

**Código de ejemplo**:
```python
# Firmar contrato
resultado = inquilino_service.firmar_contrato(
    inquilino=inquilino,
    contrato=contrato
)

if resultado:
    print("Contrato firmado exitosamente")
else:
    print("No puede firmar - sin garantía válida")
```

**Salida esperada**:
```
El inquilino Juan Pérez ha firmado el contrato N° 1
Propiedad: Av. San Martín 1500
Monto mensual: $50,000.00
Vigencia: 01/11/2025 - 01/11/2026
```

**Trazabilidad**: `main.py` líneas 199-204, `inquilino_service.py` líneas 34-72

---

### US-017: Registrar Propietarios

**Como** administrador inmobiliario
**Quiero** registrar propietarios con sus propiedades
**Para** gestionar múltiples inmuebles por dueño

#### Criterios de Aceptación

- [x] Un propietario debe tener:
    - DNI único
    - Nombre completo
    - Datos bancarios (CBU)
    - Lista de propiedades (puede estar vacía)
- [x] Un propietario puede tener múltiples propiedades
- [x] La lista de propiedades debe ser inmutable (defensive copy)
- [x] Debe poder obtener lista de propiedades
- [x] Debe poder agregar nuevas propiedades

#### Detalles Técnicos

**Clase**: `Propietario` (`python_inmobiliaria/entidades/personas/propietario.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.entidades.personas.propietario import Propietario

propiedades = [casa, departamento, finca]

# Crear propietario
propietario = Propietario(
    dni=12345678,
    nombre="María González",
    cbu="0000003100010234567890",
    propiedades=propiedades
)

# Obtener propiedades (copia inmutable)
lista_propiedades = propietario.get_propiedades()
```

**Trazabilidad**: `main.py` línea 187

---

## Epic 5: Operaciones de Negocio

### US-018: Gestionar Múltiples Propiedades

**Como** administrador de inmobiliaria
**Quiero** gestionar varias propiedades desde un servicio centralizado
**Para** tener control unificado de todo el portafolio

#### Criterios de Aceptación

- [x] El servicio debe permitir:
    - Agregar propiedades (RegistroInmobiliario)
    - Buscar propiedad por dirección
    - Buscar contratos activos
    - Generar reportes financieros
- [x] Debe manejar múltiples propiedades simultáneamente
- [x] Debe usar diccionario interno para almacenar propiedades

#### Detalles Técnicos

**Servicio**: `InmobiliariaService` (`python_inmobiliaria/servicios/negocio/inmobiliaria_service.py`)

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.negocio.inmobiliaria_service import InmobiliariaService

inmobiliaria_service = InmobiliariaService()

# Agregar propiedad
inmobiliaria_service.add_propiedad(registro)

# Buscar propiedad por dirección
propiedad = inmobiliaria_service.buscar_propiedad("Av. San Martín 1500")
```

**Trazabilidad**: `main.py` línea 225

---

### US-019: Aplicar Ajustes de Renta

**Como** administrador inmobiliario
**Quiero** aplicar ajustes de renta automáticamente
**Para** actualizar alquileres según contratos

#### Criterios de Aceptación

- [x] Debe permitir especificar:
    - Contrato a ajustar
    - Tipo de ajuste (inflacionario, fijo)
- [x] Debe actualizar monto mensual del contrato
- [x] Debe mostrar mensaje de confirmación
- [x] Si contrato vencido, manejar error apropiadamente

#### Detalles Técnicos

**Servicio**: `ContratoService.aplicar_ajuste()`

**Código de ejemplo**:
```python
# Aplicar ajuste inflacionario
contrato_service.aplicar_ajuste(contrato)

print(f"Nuevo monto: ${contrato.get_monto_mensual():,.2f}")
```

**Salida esperada**:
```
Aplicando ajuste de renta...
Monto anterior: $50,000.00
Monto actualizado: $62,500.00 (+25%)
```

**Trazabilidad**: `main.py` línea 228

---

### US-020: Renovar Contratos Automáticamente

**Como** administrador inmobiliario
**Quiero** renovar contratos vencidos automáticamente
**Para** mantener continuidad en arrendamientos

#### Criterios de Aceptación

- [x] Debe permitir renovar contratos por:
    - Número de contrato
    - Duración en meses
- [x] Debe:
    - Crear nuevo contrato con fechas actualizadas
    - Mantener inquilino y propiedad
    - Aplicar ajuste de renta según estrategia
    - Marcar contrato anterior como renovado
- [x] Usar Generics para tipo-seguridad
- [x] Permitir mostrar datos del nuevo contrato

#### Detalles Técnicos

**Servicio**: `ContratoService.renovar_contrato()`

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.contratos.contrato_service import ContratoService

# Renovar contrato por 12 meses más
nuevo_contrato = contrato_service.renovar_contrato(
    contrato_anterior=contrato,
    duracion_meses=12
)

print(f"Contrato renovado N° {nuevo_contrato.get_numero_contrato()}")
print(f"Nueva vigencia: {nuevo_contrato.get_fecha_inicio()} - {nuevo_contrato.get_fecha_vencimiento()}")
```

**Salida esperada**:
```
Renovando contrato N° 1

Nuevo contrato N° 2
Vigencia: 01/11/2026 - 01/11/2027
Monto mensual: $62,500.00
Inquilino: Juan Pérez
Propiedad: Av. San Martín 1500
```

**Trazabilidad**: `main.py` líneas 232-236

---

## Epic 6: Persistencia y Auditoría

### US-021: Persistir Registro Inmobiliario en Disco

**Como** administrador del sistema
**Quiero** guardar registros inmobiliarios en disco
**Para** mantener datos permanentes entre ejecuciones

#### Criterios de Aceptación

- [x] El sistema debe:
    - Serializar RegistroInmobiliario completo con Pickle
    - Guardar en directorio `data/`
    - Nombre de archivo: `{propietario}_{tipo_propiedad}.dat`
    - Crear directorio si no existe
    - Mostrar mensaje de confirmación
- [x] Si ocurre error, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Técnicos

**Servicio**: `RegistroInmobiliarioService.persistir()`

**Código de ejemplo**:
```python
from python_inmobiliaria.servicios.registros.registro_inmobiliario_service import RegistroInmobiliarioService

registro_service = RegistroInmobiliarioService()

# Persistir registro
registro_service.persistir(registro)
# Crea: data/Maria Gonzalez_Casa.dat
```

**Salida esperada**:
```
Registro de María González (Casa) persistido exitosamente en data/Maria Gonzalez_Casa.dat
```

**Constantes**:
```python
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
```

**Manejo de errores**:
```python
try:
    registro_service.persistir(registro)
except PersistenciaException as e:
    print(e.get_user_message())
    print(f"Archivo: {e.get_nombre_archivo()}")
    print(f"Operación: {e.get_tipo_operacion().value}")
```

**Trazabilidad**: `main.py` línea 242, `registro_inmobiliario_service.py` líneas 62-112

---

### US-022: Recuperar Registro Inmobiliario desde Disco

**Como** auditor
**Quiero** recuperar registros inmobiliarios guardados previamente
**Para** consultar históricos y realizar auditorías

#### Criterios de Aceptación

- [x] El sistema debe:
    - Deserializar archivo `.dat` con Pickle
    - Buscar en directorio `data/`
    - Validar que propietario no sea nulo/vacío
    - Retornar RegistroInmobiliario completo
    - Mostrar mensaje de confirmación
- [x] Si archivo no existe, lanzar `PersistenciaException`
- [x] Si archivo corrupto, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Técnicos

**Servicio**: `RegistroInmobiliarioService.leer_registro()` (método estático)

**Código de ejemplo**:
```python
# Leer registro persistido
registro_leido = RegistroInmobiliarioService.leer_registro(
    propietario="Maria Gonzalez",
    tipo_propiedad="Casa"
)

# Mostrar datos recuperados
registro_service.mostrar_datos(registro_leido)
```

**Salida esperada**:
```
Registro de María González (Casa) recuperado exitosamente desde data/Maria Gonzalez_Casa.dat

REGISTRO INMOBILIARIO
=====================
ID Registro:  1
Propietario:  María González
Valor Fiscal: 5500000.00
...
```

**Validaciones**:
```python
# Propietario vacío
try:
    RegistroInmobiliarioService.leer_registro("", "Casa")
except ValueError as e:
    print("El nombre del propietario no puede ser nulo o vacío")

# Archivo no existe
try:
    RegistroInmobiliarioService.leer_registro("NoExiste", "Casa")
except PersistenciaException as e:
    print(f"Archivo no encontrado: {e.get_nombre_archivo()}")
```

**Trazabilidad**: `main.py` líneas 246-247, `registro_inmobiliario_service.py` líneas 114-171

---

### US-023: Generar Reportes Financieros

**Como** contador
**Quiero** generar reportes financieros del portafolio
**Para** analizar ingresos y rentabilidad

#### Criterios de Aceptación

- [x] El sistema debe generar reportes con:
    - Listado de propiedades y valores
    - Contratos activos y montos
    - Ingresos mensuales proyectados
    - Ingresos anuales proyectados
    - Morosidad actual
- [x] Debe poder exportar en formato texto
- [x] Debe calcular totales automáticamente

#### Detalles Técnicos

**Servicio**: `InmobiliariaService.generar_reporte_financiero()`

**Código de ejemplo**:
```python
# Generar reporte financiero
reporte = inmobiliaria_service.generar_reporte_financiero()

print(reporte.get_resumen())
```

**Salida esperada**:
```
REPORTE FINANCIERO
==================
Propiedades totales: 15
Contratos activos: 12
Contratos vencidos: 2
Propiedades disponibles: 1

Ingresos mensuales: $2,150,000.00
Ingresos anuales proyectados: $25,800,000.00
Morosidad: 2 contratos ($100,000.00)
```

**Trazabilidad**: `main.py` línea 247, `inmobiliaria_service.py` líneas 28-60

---

## Historias Técnicas (Patrones de Diseño)

### US-TECH-001: Implementar Singleton para PropiedadServiceRegistry

**Como** arquitecto de software
**Quiero** garantizar una única instancia del registro de servicios
**Para** compartir estado consistente entre todos los servicios

#### Criterios de Aceptación

- [x] Implementar patrón Singleton thread-safe
- [x] Usar double-checked locking con Lock
- [x] Inicialización perezosa (lazy initialization)
- [x] Método `get_instance()` para acceso
- [x] Constructor `__new__` para controlar instanciación
- [x] NO permitir múltiples instancias

#### Detalles Técnicos

**Clase**: `PropiedadServiceRegistry`
**Patrón**: Singleton

**Implementación**:
```python
from threading import Lock

class PropiedadServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked
                    cls._instance = super().__new__(cls)
                    # Inicializar servicios una sola vez
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
```

**Uso**:
```python
# Opción 1: Instanciación directa
registry = PropiedadServiceRegistry()

# Opción 2: Método get_instance()
registry = PropiedadServiceRegistry.get_instance()

# Ambas retornan la MISMA instancia
assert registry is PropiedadServiceRegistry.get_instance()
```

**Trazabilidad**: `propiedad_service_registry.py` líneas 20-46

---

### US-TECH-002: Implementar Factory Method para Creación de Propiedades

**Como** arquitecto de software
**Quiero** centralizar creación de propiedades mediante Factory Method
**Para** desacoplar cliente de clases concretas

#### Criterios de Aceptación

- [x] Crear clase `PropiedadFactory` con método estático
- [x] Soportar creación de: Casa, Departamento, Finca
- [x] Usar diccionario de factories (no if/elif cascades)
- [x] Lanzar `ValueError` si tipo desconocido
- [x] Retornar tipo base `Propiedad` (no tipos concretos)
- [x] NO usar lambdas - usar métodos estáticos dedicados

#### Detalles Técnicos

**Clase**: `PropiedadFactory`
**Patrón**: Factory Method

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

    @staticmethod
    def _crear_casa() -> Casa:
        from python_inmobiliaria.entidades.propiedades.casa import Casa
        return Casa(terreno=250.0, plantas=2, garaje=True)

    # ... otros métodos _crear_*
```

**Uso**:
```python
from python_inmobiliaria.patrones.factory.propiedad_factory import PropiedadFactory

# Cliente NO conoce clases concretas
propiedad = PropiedadFactory.crear_propiedad("Casa")
# Retorna Propiedad (interfaz), no Casa (concreto)
```

**Trazabilidad**: `propiedad_factory.py` líneas 8-67

---

### US-TECH-003: Implementar Observer Pattern para Monitores

**Como** arquitecto de software
**Quiero** implementar patrón Observer con Generics
**Para** notificar cambios de monitores de forma tipo-segura

#### Criterios de Aceptación

- [x] Crear clase `Observable[T]` genérica
- [x] Crear interfaz `Observer[T]` genérica
- [x] Soportar múltiples observadores
- [x] Métodos: `agregar_observador()`, `eliminar_observador()`, `notificar_observadores()`
- [x] Monitores heredan de `Observable[date]`
- [x] Controlador hereda de `Observer[date]`
- [x] Thread-safe en notificaciones

#### Detalles Técnicos

**Clases**: `Observable[T]`, `Observer[T]`
**Patrón**: Observer

**Implementación**:
```python
from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso**:
```python
# Monitor es Observable[date]
class FechaMonitorTask(threading.Thread, Observable[date]):
    def run(self):
        while not self._detenido.is_set():
            fecha = date.today()
            self.notificar_observadores(fecha)  # Notifica date

# Controlador es Observer[date]
class ControlVencimientoTask(Observer[date]):
    def actualizar(self, evento: date) -> None:
        self._fecha_actual = evento  # Recibe date
```

**Trazabilidad**: `observable.py`, `observer.py`

---

### US-TECH-004: Implementar Strategy Pattern para Ajustes de Renta

**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de ajuste
**Para** permitir diferentes estrategias según tipo de contrato

#### Criterios de Aceptación

- [x] Crear interfaz `AjusteRentaStrategy` abstracta
- [x] Implementar `AjusteInflacionarioStrategy` (contratos anuales)
- [x] Implementar `AjusteFijoStrategy` (contratos con ajuste pactado)
- [x] Inyectar estrategia en constructor de servicios
- [x] Servicios delegan cálculo a estrategia
- [x] Estrategias usan constantes de `constantes.py`

#### Detalles Técnicos

**Interfaz**: `AjusteRentaStrategy`
**Implementaciones**: `AjusteInflacionarioStrategy`, `AjusteFijoStrategy`
**Patrón**: Strategy

**Implementación**:
```python
# Interfaz
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
        meses = self._calcular_meses(contrato.get_fecha_inicio(), fecha_ajuste)
        if meses >= MESES_AJUSTE_CONTRATO:
            return monto_actual * AJUSTE_INFLACION_ANUAL
        else:
            return monto_actual

# Estrategia 2: Fijo
class AjusteFijoStrategy(AjusteRentaStrategy):
    def __init__(self, porcentaje: float):
        self._porcentaje = porcentaje

    def calcular_ajuste(self, monto_actual, fecha_ajuste, contrato):
        return monto_actual * (1 + self._porcentaje)
```

**Inyección**:
```python
class ContratoService:
    def __init__(self):
        super().__init__(AjusteInflacionarioStrategy())  # Inyección

class ContratoFijoService:
    def __init__(self):
        super().__init__(AjusteFijoStrategy(0.10))  # Inyección
```

**Delegación**:
```python
class ContratoService:
    def aplicar_ajuste(self, contrato: 'Contrato') -> float:
        # Delegar a estrategia
        nuevo_monto = self._estrategia_ajuste.calcular_ajuste(
            contrato.get_monto_mensual(),
            date.today(),
            contrato
        )
        contrato.set_monto_mensual(nuevo_monto)
        return nuevo_monto
```

**Trazabilidad**: `ajuste_inflacionario_strategy.py`, `ajuste_fijo_strategy.py`, `contrato_service.py` líneas 35-59

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimórfico

**Como** arquitecto de software
**Quiero** eliminar cascadas de isinstance()
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptación

- [x] Crear diccionarios de handlers por tipo
- [x] Registrar handler para cada tipo de propiedad
- [x] Método `calcular_valor()` usa dispatch automático
- [x] Método `mostrar_datos()` usa dispatch automático
- [x] Lanzar error si tipo no registrado
- [x] NO usar lambdas - usar métodos de instancia dedicados

#### Detalles Técnicos

**Clase**: `PropiedadServiceRegistry`
**Patrón**: Registry

**Implementación**:
```python
class PropiedadServiceRegistry:
    def __init__(self):
        # Diccionarios de handlers
        self._calcular_valor_handlers = {
            Casa: self._calcular_valor_casa,
            Departamento: self._calcular_valor_departamento,
            Finca: self._calcular_valor_finca
        }

        self._mostrar_datos_handlers = {
            Casa: self._mostrar_datos_casa,
            Departamento: self._mostrar_datos_departamento,
            Finca: self._mostrar_datos_finca
        }

    def calcular_valor(self, propiedad: Propiedad) -> float:
        tipo = type(propiedad)
        if tipo not in self._calcular_valor_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._calcular_valor_handlers[tipo](propiedad)

    # Handlers dedicados (NO lambdas)
    def _calcular_valor_casa(self, propiedad):
        return self._casa_service.calcular_valor(propiedad)
```

**Ventajas**:
- Sin `isinstance()` cascades
- Fácil agregar nuevos tipos
- Mejor rendimiento (O(1) lookup)
- Más testeable

**Trazabilidad**: `propiedad_service_registry.py` líneas 48-89

---

## Resumen de Cobertura Funcional

### Totales por Epic

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: Propiedades y Contratos | 3 | 3 | 100% |
| Epic 2: Gestión de Propiedades | 6 | 6 | 100% |
| Epic 3: Monitoreo Automatizado | 4 | 4 | 100% |
| Epic 4: Gestión de Personas | 4 | 4 | 100% |
| Epic 5: Operaciones de Negocio | 3 | 3 | 100% |
| Epic 6: Persistencia y Auditoría | 3 | 3 | 100% |
| Historias Técnicas (Patrones) | 5 | 5 | 100% |
| **TOTAL** | **28** | **28** | **100%** |

### Patrones de Diseño Cubiertos

- [x] SINGLETON - PropiedadServiceRegistry
- [x] FACTORY METHOD - PropiedadFactory
- [x] OBSERVER - Monitores y eventos
- [x] STRATEGY - Ajuste de renta
- [x] REGISTRY - Dispatch polimórfico (bonus)

### Funcionalidades Completas

- [x] Gestión de 3 tipos de propiedades
- [x] Sistema de monitoreo automatizado con 3 threads
- [x] Gestión de inquilinos con garantías
- [x] Persistencia con Pickle
- [x] Operaciones de negocio de alto nivel
- [x] Manejo de excepciones específicas
- [x] PEP 8 compliance 100%
- [x] Type hints con TYPE_CHECKING
- [x] Constantes centralizadas
- [x] Código limpio sin lambdas

---

**Última actualización**: Noviembre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%