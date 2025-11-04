# Rúbrica de Evaluación Técnica - Sistema de Gestión de Arrendamientos y Contratos

**Proyecto**: PythonInmobiliaria
**Versión**: 1.0.0
**Fecha**: Noviembre 2025
**Tipo de Evaluación**: Técnica Académica / Profesional

---

## Instrucciones de Uso

Esta rúbrica está diseñada para evaluar proyectos de software de gestión inmobiliaria que implementen patrones de diseño en Python. Se utiliza para:

1. **Evaluación académica**: Proyectos de estudiantes en cursos de Ingeniería de Software
2. **Evaluación técnica**: Entrevistas técnicas para desarrolladores
3. **Code review**: Revisión de calidad de código en proyectos profesionales
4. **Autoevaluación**: Chequeo de cumplimiento de buenas prácticas

### Escala de Puntuación

- **Excelente (4 puntos)**: Cumple completamente con criterio, implementación superior
- **Bueno (3 puntos)**: Cumple con criterio, implementación correcta con mínimos detalles
- **Suficiente (2 puntos)**: Cumple parcialmente, implementación funcional con deficiencias
- **Insuficiente (1 punto)**: No cumple o cumplimiento mínimo, implementación deficiente
- **No Implementado (0 puntos)**: Criterio no implementado

### Puntaje Total

- **Puntaje Máximo**: 260 puntos
- **Puntaje de Aprobación**: 182 puntos (70%)
- **Puntaje de Excelencia**: 234 puntos (90%)

---

## Sección 1: Patrones de Diseño (80 puntos)

### 1.1 Patrón SINGLETON (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementación correcta del patrón** | 5 | Clase implementa Singleton con instancia única | `__new__` con control de instancia única |
| **Thread-safety** | 5 | Implementación thread-safe con Lock | Uso de `threading.Lock` con double-checked locking |
| **Acceso consistente** | 3 | Método `get_instance()` disponible | Método de clase que retorna instancia |
| **Inicialización perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (Registry) | PropiedadServiceRegistry es Singleton |

**Puntaje Sección 1.1**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementación de Singleton]
```

---

### 1.2 Patrón FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementación correcta del patrón** | 5 | Factory encapsula creación de objetos | Método estático `crear_propiedad(tipo)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Propiedad`, no tipos concretos |
| **Extensibilidad** | 4 | Fácil agregar nuevos tipos | Diccionario de factories, no if/elif cascades |
| **Validación de entrada** | 3 | Valida parámetros y lanza excepciones | Lanza `ValueError` si tipo desconocido |
| **Uso apropiado en el sistema** | 3 | Factory usado en servicios (InmobiliariaService) | `registrar_propiedad()` usa factory internamente |

**Puntaje Sección 1.2**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementación de Factory]
```

---

### 1.3 Patrón OBSERVER (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementación correcta del patrón** | 5 | Observable y Observer implementados | Clases `Observable[T]` y `Observer[T]` |
| **Generics para tipo-seguridad** | 5 | Uso de TypeVar y Generic[T] | `Observable[date]`, `Observer[date]` |
| **Notificaciones automáticas** | 4 | Observadores notificados al cambiar estado | `notificar_observadores()` llamado en monitores |
| **Desacoplamiento** | 3 | Observable no conoce detalles de Observer | Lista genérica de observadores |
| **Uso apropiado en el sistema** | 3 | Monitores como Observable, Control como Observer | FechaMonitorTask, ControlVencimientoTask |

**Puntaje Sección 1.3**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementación de Observer]
```

---

### 1.4 Patrón STRATEGY (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementación correcta del patrón** | 5 | Interfaz Strategy con implementaciones | `AjusteRentaStrategy` (abstracta) |
| **Algoritmos intercambiables** | 5 | Múltiples estrategias implementadas | `AjusteInflacionarioStrategy`, `AjusteFijoStrategy` |
| **Inyección de dependencias** | 4 | Estrategia inyectada vía constructor | Servicios reciben strategy en `__init__` |
| **Delegación correcta** | 3 | Servicios delegan cálculo a estrategia | `calcular_ajuste()` llamado desde servicio |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas según tipo de contrato | Anuales: inflacionario, Fijos: porcentaje fijo |

**Puntaje Sección 1.4**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementación de Strategy]
```

---

**PUNTAJE TOTAL SECCIÓN 1**: _____ / 80

---

## Sección 2: Arquitectura y Diseño (60 puntos)

### 2.1 Separación de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo lógica | Clases en `entidades/` vs `servicios/` |
| **Service Layer Pattern** | 5 | Capa de servicios bien definida | Servicios contienen toda la lógica de negocio |
| **Principio SRP** | 4 | Cada clase una única responsabilidad | Una clase = un concepto de dominio |
| **Cohesión alta** | 3 | Elementos relacionados agrupados | Módulos temáticos (propiedades, contratos, personas) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces, inyección de dependencias |

**Puntaje Sección 2.1**: _____ / 20

---

### 2.2 Jerarquía de Clases (15 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Herencia apropiada** | 5 | Jerarquía lógica de clases | `PropiedadService` → `InmuebleService` → servicios específicos |
| **Eliminación de duplicación** | 4 | Código compartido en clases base | `calcular_valor()` en `PropiedadService` base |
| **Polimorfismo** | 3 | Subtipos intercambiables | Todas las propiedades son `Propiedad` |
| **Interfaces bien definidas** | 3 | Contratos claros entre clases | Métodos abstractos en clases base |

**Puntaje Sección 2.2**: _____ / 15

---

### 2.3 Manejo de Excepciones (15 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Jerarquía de excepciones** | 5 | Excepciones personalizadas heredan de base | `InmobiliariaException` base |
| **Excepciones específicas** | 4 | Excepciones de dominio implementadas | `ContratoVencidoException`, `PagoInsuficienteException`, `PersistenciaException` |
| **Mensajes descriptivos** | 3 | Mensajes claros para usuario y técnico | Separación user_message / technical_message |
| **Uso apropiado** | 3 | Excepciones usadas en puntos correctos | Validaciones lanzan excepciones apropiadas |

**Puntaje Sección 2.3**: _____ / 15

---

### 2.4 Organización del Código (10 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Estructura de paquetes** | 3 | Organización lógica de módulos | Paquetes: entidades, servicios, patrones, monitoreo, excepciones |
| **Módulos temáticos** | 3 | Agrupación por dominio | propiedades/, contratos/, personas/ |
| **Archivos `__init__.py`** | 2 | Inicialización de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Uso de TYPE_CHECKING para forward references |

**Puntaje Sección 2.4**: _____ / 10

---

**PUNTAJE TOTAL SECCIÓN 2**: _____ / 60

---

## Sección 3: Calidad de Código (60 puntos)

### 3.1 PEP 8 Compliance (20 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Nombres de variables** | 4 | snake_case, descriptivos, sin abreviaciones | `monto_mensual` no `monto`, `fecha_vencimiento` no `fec_venc` |
| **Nombres de clases** | 3 | PascalCase consistente | `PropiedadFactory`, `ContratoService` |
| **Nombres de constantes** | 3 | UPPER_SNAKE_CASE en módulo centralizado | Todas en `constantes.py` |
| **Organización de imports** | 4 | PEP 8: Standard → Third-party → Local | Secciones comentadas |
| **Longitud de línea** | 2 | Máximo 100-120 caracteres | No líneas excesivamente largas |
| **Espaciado y formato** | 4 | Espaciado consistente según PEP 8 | 2 líneas entre clases, 1 entre métodos |

**Puntaje Sección 3.1**: _____ / 20

---

### 3.2 Documentación (15 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Docstrings en clases** | 4 | Todas las clases documentadas | Docstring en cada clase pública |
| **Docstrings en métodos** | 4 | Métodos públicos documentados | Google Style: Args, Returns, Raises |
| **Formato Google Style** | 3 | Estilo consistente (NO JavaDoc) | Args: / Returns: / Raises: |
| **Comentarios en código complejo** | 2 | Explicación de lógica no obvia | Comentarios donde necesario |
| **README y documentación externa** | 2 | Documentación de proyecto completa | README.md, USER_STORIES.md |

**Puntaje Sección 3.2**: _____ / 15

---

### 3.3 Type Hints (10 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Type hints en firmas** | 4 | Parámetros y retornos tipados | `def metodo(param: str) -> int:` |
| **Uso de TYPE_CHECKING** | 3 | Evita imports circulares | `if TYPE_CHECKING: from ...` |
| **Generics donde apropiado** | 3 | TypeVar y Generic[T] usados | `Observable[T]`, `Reporte[T]` |

**Puntaje Sección 3.3**: _____ / 10

---

### 3.4 Principios de Código Limpio (15 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **NO magic numbers** | 5 | Constantes centralizadas | CERO valores hardcodeados |
| **NO lambdas** | 4 | Funciones/métodos nombrados | Métodos estáticos en lugar de lambdas |
| **Funciones pequeñas** | 3 | Métodos con responsabilidad única | Funciones < 30 líneas idealmente |
| **Nombres descriptivos** | 3 | Variables y métodos autoexplicativos | `calcular_ajuste()` no `calc()` |

**Puntaje Sección 3.4**: _____ / 15

---

**PUNTAJE TOTAL SECCIÓN 3**: _____ / 60

---

## Sección 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestión de Propiedades (12 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Múltiples tipos de propiedades** | 4 | Al menos 3 tipos implementados | Casa, Departamento, Finca |
| **Registro funcional** | 4 | Sistema registra y valida propiedades | `registrar_propiedad()` con validación |
| **Cálculo de valores** | 4 | Valuación automática de propiedades | `calcular_valor()` diferenciado por tipo |

**Puntaje Sección 4.1**: _____ / 12

---

### 4.2 Sistema de Monitoreo Automatizado (12 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Monitores operativos** | 4 | Fecha y pagos en threads | Verificaciones periódicas |
| **Control automático** | 4 | Alertas basadas en condiciones | Evalúa vencimientos y morosidad |
| **Graceful shutdown** | 4 | Detención limpia de threads | Uso de Event y timeout |

**Puntaje Sección 4.2**: _____ / 12

---

### 4.3 Gestión de Contratos y Pagos (8 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Contratos y renovaciones** | 4 | Sistema crea y renueva contratos | `crear_contrato()`, `renovar_contrato()` |
| **Registro de pagos** | 4 | Validación de pagos y actualización | Verifica monto antes de registrar |

**Puntaje Sección 4.3**: _____ / 8

---

### 4.4 Persistencia (8 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Guardado funcional** | 4 | Registros persisten en disco | `persistir()` crea archivo .dat |
| **Lectura funcional** | 4 | Registros recuperados correctamente | `leer_registro()` deserializa |

**Puntaje Sección 4.4**: _____ / 8

---

**PUNTAJE TOTAL SECCIÓN 4**: _____ / 40

---

## Sección 5: Buenas Prácticas Avanzadas (20 puntos)

### 5.1 Threading y Concurrencia (10 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Threads daemon** | 3 | Threads de fondo como daemon | `daemon=True` |
| **Thread-safety** | 4 | Operaciones thread-safe donde necesario | Lock en Singleton, Event en threads |
| **Manejo de recursos** | 3 | Cierre apropiado de threads | `join()` con timeout |

**Puntaje Sección 5.1**: _____ / 10

---

### 5.2 Validación y Robustez (10 puntos)

| Criterio | Puntos | Descripción | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Validación de entrada** | 4 | Parámetros validados en setters | Monto > 0, fechas válidas |
| **Defensive copying** | 3 | Listas inmutables donde apropiado | `get_propiedades()` retorna copia |
| **Manejo de errores** | 3 | Try/except apropiados | Persistencia con manejo de IOError |

**Puntaje Sección 5.2**: _____ / 10

---

**PUNTAJE TOTAL SECCIÓN 5**: _____ / 20

---

## Resumen de Evaluación

### Desglose por Sección

| Sección | Puntaje Obtenido | Puntaje Máximo | Porcentaje |
|---------|------------------|----------------|------------|
| 1. Patrones de Diseño | _____ | 80 | _____% |
| 2. Arquitectura y Diseño | _____ | 60 | _____% |
| 3. Calidad de Código | _____ | 60 | _____% |
| 4. Funcionalidad del Sistema | _____ | 40 | _____% |
| 5. Buenas Prácticas Avanzadas | _____ | 20 | _____% |
| **TOTAL** | **_____** | **260** | **_____%** |

### Calificación Final

| Rango de Puntaje | Calificación | Descripción |
|------------------|--------------|-------------|
| 234 - 260 (90%+) | **Excelente** | Implementación profesional de alta calidad |
| 208 - 233 (80-89%) | **Muy Bueno** | Implementación sólida con prácticas avanzadas |
| 182 - 207 (70-79%) | **Bueno** | Implementación correcta que cumple requisitos |
| 156 - 181 (60-69%) | **Suficiente** | Implementación funcional con deficiencias |
| 0 - 155 (<60%) | **Insuficiente** | Requiere mejoras significativas |

**CALIFICACIÓN FINAL**: ________________

---

## Comentarios Generales del Evaluador

### Fortalezas Identificadas
```
[Espacio para comentarios sobre aspectos destacados del proyecto]

Ejemplo:
- Excelente implementación de patrones de diseño
- Código muy limpio y bien documentado
- Arquitectura bien pensada para el dominio inmobiliario
```

### Áreas de Mejora
```
[Espacio para comentarios sobre aspectos a mejorar]

Ejemplo:
- Faltan tests unitarios
- Documentación de API podría ser más detallada
- Considerar agregar logging para auditoría
```

### Recomendaciones
```
[Espacio para recomendaciones específicas]

Ejemplo:
- Agregar tests con pytest
- Implementar patrón Command para deshacer operaciones
- Considerar persistencia con base de datos relacional (SQLite/PostgreSQL)
- Agregar generación de reportes en PDF
```

---

## Criterios de Evaluación Detallados

### Patrón SINGLETON - Checklist Detallado

- [ ] Clase tiene atributo `_instance` de clase
- [ ] Método `__new__` implementado para controlar instanciación
- [ ] Thread-safe con `threading.Lock`
- [ ] Double-checked locking correctamente implementado
- [ ] Método `get_instance()` disponible
- [ ] Inicialización perezosa (lazy)
- [ ] Una sola instancia garantizada
- [ ] Usado apropiadamente (Registry, no en todas las clases)

### Patrón FACTORY METHOD - Checklist Detallado

- [ ] Método factory es estático
- [ ] Recibe parámetro para determinar tipo a crear
- [ ] Retorna tipo base/interfaz, no tipo concreto
- [ ] Cliente NO importa clases concretas
- [ ] Usa diccionario de factories (NO if/elif)
- [ ] Fácil agregar nuevos tipos sin modificar factory
- [ ] Validación de parámetros con excepciones
- [ ] Usado en servicios (InmobiliariaService.registrar_propiedad)

### Patrón OBSERVER - Checklist Detallado

- [ ] Interfaz `Observer[T]` con método `actualizar(evento: T)`
- [ ] Clase `Observable[T]` con lista de observadores
- [ ] Método `agregar_observador(observador: Observer[T])`
- [ ] Método `eliminar_observador(observador: Observer[T])`
- [ ] Método `notificar_observadores(evento: T)`
- [ ] Uso de Generics (TypeVar, Generic[T])
- [ ] Monitores heredan de Observable
- [ ] Controlador hereda de Observer
- [ ] Notificaciones automáticas al cambiar estado

### Patrón STRATEGY - Checklist Detallado

- [ ] Interfaz `Strategy` abstracta con método abstracto
- [ ] Al menos 2 implementaciones concretas
- [ ] Estrategia inyectada vía constructor
- [ ] Servicios delegan cálculo a estrategia
- [ ] Estrategias intercambiables sin modificar cliente
- [ ] Sin condicionales if/else para seleccionar algoritmo
- [ ] Estrategias usan constantes (no magic numbers)
- [ ] Usado apropiadamente según tipo de contrato

### PEP 8 - Checklist Detallado

- [ ] Nombres de variables: snake_case, sin abreviaciones
- [ ] Nombres de clases: PascalCase
- [ ] Nombres de constantes: UPPER_SNAKE_CASE
- [ ] Imports organizados: Standard → Third-party → Local
- [ ] Docstrings en Google Style (NO JavaDoc)
- [ ] Líneas max 100-120 caracteres
- [ ] 2 líneas en blanco entre clases
- [ ] 1 línea en blanco entre métodos
- [ ] Type hints en todas las firmas públicas
- [ ] Uso de TYPE_CHECKING para forward references

### Código Limpio - Checklist Detallado

- [ ] CERO magic numbers (todas en constantes.py)
- [ ] CERO lambdas (usar funciones/métodos nombrados)
- [ ] Funciones pequeñas (<30 líneas idealmente)
- [ ] Nombres descriptivos (no abreviaciones)
- [ ] Un nivel de abstracción por función
- [ ] Sin código duplicado
- [ ] Comentarios solo donde necesario (código autoexplicativo)
- [ ] Sin código muerto (comentado o sin usar)

---

## Anexo: Mapeo de Historias de Usuario a Criterios

### Epic 1: Propiedades y Contratos
- **US-001**: Sección 4.1 (Gestión de Propiedades)
- **US-002**: Sección 4.3 (Gestión de Contratos)
- **US-003**: Sección 4.4 (Persistencia)

### Epic 2: Gestión de Propiedades Inmobiliarias
- **US-004 a US-009**: Sección 4.1 (Gestión de Propiedades), Sección 1.2 (Factory), Sección 1.4 (Strategy)

### Epic 3: Monitoreo Automatizado
- **US-010 a US-013**: Sección 4.2 (Monitoreo Automatizado), Sección 1.3 (Observer), Sección 5.1 (Threading)

### Epic 4: Gestión de Personas
- **US-014 a US-017**: Sección 4.3 (Gestión de Contratos), Sección 2.1 (Separación de Responsabilidades)

### Epic 5: Operaciones de Negocio
- **US-018 a US-020**: Sección 4.1 (Gestión de Propiedades), Sección 4.3 (Gestión de Contratos)

### Epic 6: Persistencia y Auditoría
- **US-021 a US-023**: Sección 4.4 (Persistencia), Sección 2.3 (Manejo de Excepciones)

### Historias Técnicas
- **US-TECH-001**: Sección 1.1 (Singleton)
- **US-TECH-002**: Sección 1.2 (Factory)
- **US-TECH-003**: Sección 1.3 (Observer)
- **US-TECH-004**: Sección 1.4 (Strategy)
- **US-TECH-005**: Sección 2.1 (Arquitectura)

---

## Instrucciones para el Evaluador

### Antes de Evaluar

1. **Leer documentación**: README.md, USER_STORIES.md, CLAUDE.md (si existe)
2. **Ejecutar sistema**: `python main.py` debe completar exitosamente
3. **Revisar estructura**: Verificar organización de paquetes
4. **Identificar patrones**: Localizar implementaciones de cada patrón

### Durante la Evaluación

1. **Marcar checkboxes**: Usar checklists detallados por patrón
2. **Asignar puntajes**: Ser objetivo según escala de puntuación
3. **Tomar notas**: Documentar fortalezas y áreas de mejora
4. **Buscar evidencias**: Verificar que criterios se cumplan en código

### Después de Evaluar

1. **Calcular totales**: Sumar puntajes por sección
2. **Determinar calificación**: Según tabla de rangos
3. **Escribir comentarios**: Feedback constructivo y específico
4. **Dar recomendaciones**: Sugerencias concretas de mejora

### Criterios de Objetividad

- **Evidencia en código**: Solo puntuar lo que está implementado
- **No suponer**: Si no se ve, no está
- **Ser consistente**: Aplicar mismos criterios a todos los proyectos
- **Documentar decisiones**: Justificar puntajes en comentarios

---

## Criterios Específicos del Dominio Inmobiliario

### Validaciones de Negocio

- [ ] **Contratos**: Fechas de inicio < fechas de vencimiento
- [ ] **Pagos**: Montos positivos, fechas válidas
- [ ] **Propiedades**: Superficies positivas, direcciones válidas
- [ ] **Garantías**: Montos suficientes (típicamente 2 meses de alquiler)
- [ ] **Ajustes**: Aplicados según periodicidad contractual
- [ ] **Vencimientos**: Alertas generadas con anticipación (30 días)

### Lógica de Negocio Específica

- [ ] **Cálculo de valores**: Diferenciado por tipo de propiedad
- [ ] **Ajustes de renta**: Inflacionario o fijo según contrato
- [ ] **Renovaciones**: Mantienen inquilino y propiedad, actualizan fechas
- [ ] **Morosidad**: Control de pagos atrasados
- [ ] **Disponibilidad**: Control de propiedades ocupadas vs disponibles
- [ ] **Referencias**: Validación de inquilinos antes de contrato

### Reportes y Auditoría

- [ ] **Reportes financieros**: Ingresos proyectados mensuales/anuales
- [ ] **Estado de contratos**: Activos, vencidos, próximos a vencer
- [ ] **Morosidad**: Listado de inquilinos con pagos atrasados
- [ ] **Disponibilidad**: Propiedades disponibles para alquiler
- [ ] **Histórico**: Trazabilidad de contratos anteriores
- [ ] **Persistencia**: Registros completos guardados y recuperables

---

## Evaluación de Características Avanzadas (Bonus)

### Características Opcionales que Suman Puntos Adicionales

| Característica | Puntos Bonus | Descripción |
|----------------|--------------|-------------|
| Tests unitarios con pytest | +10 | Coverage > 70% |
| Tests de integración | +5 | Flujos completos testeados |
| Logging estructurado | +5 | Uso de logging para auditoría |
| Base de datos relacional | +10 | SQLite o PostgreSQL en lugar de Pickle |
| API REST | +15 | Endpoints para operaciones principales |
| Interfaz gráfica | +15 | GUI con tkinter o Qt |
| Generación de PDFs | +5 | Contratos y recibos en PDF |
| Envío de emails | +5 | Notificaciones automáticas por email |
| CI/CD Pipeline | +10 | GitHub Actions o similar |
| Docker containerization | +5 | Dockerfile y docker-compose |

**Puntaje Bonus Total**: _____ / 100 (opcional)

**Puntaje Final con Bonus**: _____ / 360

---

## Notas Adicionales para Evaluadores

### Aspectos Críticos del Dominio Inmobiliario

1. **Validación de fechas**: Fundamental para contratos y vencimientos
2. **Cálculos monetarios**: Usar Decimal en lugar de float en producción
3. **Auditoría**: Trazabilidad de todas las operaciones financieras
4. **Seguridad**: Protección de datos personales (GDPR/LOPD)
5. **Persistencia**: Backup y recuperación de datos críticos

### Sugerencias de Mejora Comunes

1. **Tests**: Agregar suite de tests completa
2. **Validaciones**: Más validaciones de negocio (ej: fecha inicio < vencimiento)
3. **Logging**: Sistema de logging para auditoría
4. **Configuración**: Archivo de configuración externo (YAML/JSON)
5. **Base de datos**: Migrar de Pickle a base de datos relacional
6. **Reportes**: Más reportes (ocupación, rentabilidad, proyecciones)
7. **Notificaciones**: Sistema de notificaciones (email, SMS)
8. **Documentación**: Documentación de API con Sphinx

### Preguntas de Entrevista Técnica Sugeridas

1. ¿Por qué elegiste Singleton para PropiedadServiceRegistry?
2. ¿Cómo agregarías un nuevo tipo de propiedad (ej: Local Comercial)?
3. ¿Qué ventajas tiene Strategy para ajustes de renta vs if/else?
4. ¿Cómo harías thread-safe la actualización de pagos?
5. ¿Qué mejoras harías para producción?
6. ¿Cómo implementarías búsqueda de propiedades por criterios?
7. ¿Qué patrón usarías para deshacer operaciones (ej: cancelar pago)?
8. ¿Cómo escalarías el sistema para múltiples inmobiliarias?

---

**Evaluador**: ________________________________
**Fecha de Evaluación**: ____________________
**Firma**: ___________________________________

---

**Versión de Rúbrica**: 1.0.0
**Última Actualización**: Noviembre 2025
**Proyecto de Referencia**: PythonInmobiliaria v1.0.0