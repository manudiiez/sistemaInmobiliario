# Rúbrica de Evaluación Automatizada - Compatible con n8n

**Proyecto**: PythonInmobiliaria
**Versión**: 1.0.0
**Fecha**: Noviembre 2025
**Propósito**: Automatización de corrección de proyectos en n8n

---

## Introducción

Este documento define criterios de evaluación automatizables mediante n8n para proyectos de software de gestión inmobiliaria que implementen patrones de diseño. Cada criterio incluye:

1. **ID único**: Para referencia en workflows de n8n
2. **Tipo de verificación**: Estática (código) o Dinámica (ejecución)
3. **Método de detección**: Cómo automatizar la verificación
4. **Comando/Regex**: Script o patrón para ejecutar
5. **Puntaje**: Puntos asignados al criterio
6. **Threshold**: Umbral de aprobación

---

## Formato JSON para n8n

Cada criterio se puede representar en JSON para workflows de n8n:

```json
{
  "criterio_id": "SING-001",
  "categoria": "Singleton",
  "descripcion": "Verificar implementación de Singleton",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -r '_instance = None' --include='*.py'",
  "puntaje_max": 5,
  "threshold": 1,
  "peso": "critico"
}
```

---

## Sección 1: Verificaciones Estáticas (Análisis de Código)

### 1.1 Patrón SINGLETON

#### SING-001: Atributo de Instancia Única
```json
{
  "id": "SING-001",
  "categoria": "Singleton",
  "descripcion": "Verificar atributo _instance en clase",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '_instance = None' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

**Validación esperada**: Al menos 1 coincidencia en archivo `*registry*.py`

---

#### SING-002: Método __new__ Implementado
```json
{
  "id": "SING-002",
  "categoria": "Singleton",
  "descripcion": "Verificar método __new__ para control de instancia",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def __new__' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### SING-003: Thread-Safety con Lock
```json
{
  "id": "SING-003",
  "categoria": "Singleton",
  "descripcion": "Verificar uso de threading.Lock",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'threading.Lock\\|from threading import Lock' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### SING-004: Método get_instance()
```json
{
  "id": "SING-004",
  "categoria": "Singleton",
  "descripcion": "Verificar método get_instance()",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def get_instance' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "medio"
}
```

---

### 1.2 Patrón FACTORY METHOD

#### FACT-001: Método Factory Estático
```json
{
  "id": "FACT-001",
  "categoria": "Factory",
  "descripcion": "Verificar método factory estático",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '@staticmethod' --include='*factory*.py' .",
  "puntaje": 3,
  "threshold": 2,
  "peso": "critico"
}
```

---

#### FACT-002: Clase Factory Existe
```json
{
  "id": "FACT-002",
  "categoria": "Factory",
  "descripcion": "Verificar existencia de clase Factory",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name '*factory*.py' -type f",
  "puntaje": 2,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### FACT-003: Método crear_* Implementado
```json
{
  "id": "FACT-003",
  "categoria": "Factory",
  "descripcion": "Verificar métodos de creación",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def crear_\\|def _crear_' --include='*factory*.py' .",
  "puntaje": 3,
  "threshold": 3,
  "peso": "alto"
}
```

---

#### FACT-004: Diccionario de Factories
```json
{
  "id": "FACT-004",
  "categoria": "Factory",
  "descripcion": "Verificar uso de diccionario para dispatch",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'factories = {' --include='*factory*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "medio"
}
```

---

### 1.3 Patrón OBSERVER

#### OBSR-001: Clase Observable Existe
```json
{
  "id": "OBSR-001",
  "categoria": "Observer",
  "descripcion": "Verificar clase Observable",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Observable' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### OBSR-002: Clase Observer Existe
```json
{
  "id": "OBSR-002",
  "categoria": "Observer",
  "descripcion": "Verificar interfaz Observer",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Observer' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### OBSR-003: Uso de Generics
```json
{
  "id": "OBSR-003",
  "categoria": "Observer",
  "descripcion": "Verificar uso de Generic[T]",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'Generic\\[T\\]\\|Observable\\[' --include='*.py' .",
  "puntaje": 4,
  "threshold": 2,
  "peso": "alto"
}
```

---

#### OBSR-004: Método notificar_observadores
```json
{
  "id": "OBSR-004",
  "categoria": "Observer",
  "descripcion": "Verificar método de notificación",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def notificar_observadores' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

---

### 1.4 Patrón STRATEGY

#### STRT-001: Interfaz Strategy Abstracta
```json
{
  "id": "STRT-001",
  "categoria": "Strategy",
  "descripcion": "Verificar interfaz Strategy abstracta",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class.*Strategy.*ABC' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### STRT-002: Implementaciones de Strategy
```json
{
  "id": "STRT-002",
  "categoria": "Strategy",
  "descripcion": "Verificar al menos 2 implementaciones",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'Strategy):' --include='*.py' .",
  "puntaje": 4,
  "threshold": 2,
  "peso": "critico"
}
```

---

#### STRT-003: Inyección de Estrategia
```json
{
  "id": "STRT-003",
  "categoria": "Strategy",
  "descripcion": "Verificar inyección vía constructor",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'self._estrategia\\|estrategia:' --include='*service*.py' .",
  "puntaje": 3,
  "threshold": 2,
  "peso": "alto"
}
```

---

### 1.5 Calidad de Código

#### QUAL-001: Constantes Centralizadas
```json
{
  "id": "QUAL-001",
  "categoria": "Calidad",
  "descripcion": "Verificar archivo constantes.py existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name 'constantes.py' -type f",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### QUAL-002: NO Lambdas
```json
{
  "id": "QUAL-002",
  "categoria": "Calidad",
  "descripcion": "Verificar ausencia de lambdas",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'lambda ' --include='*.py' . | wc -l",
  "puntaje": 2,
  "threshold": 0,
  "peso": "medio",
  "inverted": true
}
```

**Nota**: `inverted: true` significa que 0 coincidencias es BUENO

---

#### QUAL-003: Type Hints
```json
{
  "id": "QUAL-003",
  "categoria": "Calidad",
  "descripcion": "Verificar uso de type hints",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def.*->\\|: str\\|: int\\|: float' --include='*.py' . | wc -l",
  "puntaje": 3,
  "threshold": 50,
  "peso": "medio"
}
```

---

#### QUAL-004: Docstrings Google Style
```json
{
  "id": "QUAL-004",
  "categoria": "Calidad",
  "descripcion": "Verificar docstrings Google Style (Args:)",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'Args:' --include='*.py' . | wc -l",
  "puntaje": 2,
  "threshold": 20,
  "peso": "bajo"
}
```

---

#### QUAL-005: Organización de Imports
```json
{
  "id": "QUAL-005",
  "categoria": "Calidad",
  "descripcion": "Verificar comentarios de sección en imports",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '# Standard library\\|# Local application' --include='*.py' . | wc -l",
  "puntaje": 2,
  "threshold": 10,
  "peso": "bajo"
}
```

---

### 1.6 Estructura del Proyecto

#### STRC-001: Paquete entidades/
```json
{
  "id": "STRC-001",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete entidades existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'entidades'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### STRC-002: Paquete servicios/
```json
{
  "id": "STRC-002",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete servicios existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'servicios'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### STRC-003: Paquete patrones/
```json
{
  "id": "STRC-003",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete patrones existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'patrones'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### STRC-004: Archivos __init__.py
```json
{
  "id": "STRC-004",
  "categoria": "Estructura",
  "descripcion": "Verificar archivos __init__.py en paquetes",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name '__init__.py' -type f | wc -l",
  "puntaje": 2,
  "threshold": 10,
  "peso": "medio"
}
```

---

### 1.7 Dominio Inmobiliario

#### DOM-001: Entidades de Propiedades
```json
{
  "id": "DOM-001",
  "categoria": "Dominio",
  "descripcion": "Verificar entidades de propiedades (Casa, Departamento, Finca)",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Casa\\|class Departamento\\|class Finca' --include='*.py' .",
  "puntaje": 3,
  "threshold": 3,
  "peso": "critico"
}
```

---

#### DOM-002: Entidad Contrato
```json
{
  "id": "DOM-002",
  "categoria": "Dominio",
  "descripcion": "Verificar entidad Contrato existe",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Contrato' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### DOM-003: Entidad Inquilino
```json
{
  "id": "DOM-003",
  "categoria": "Dominio",
  "descripcion": "Verificar entidad Inquilino existe",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Inquilino' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### DOM-004: Entidad Propietario
```json
{
  "id": "DOM-004",
  "categoria": "Dominio",
  "descripcion": "Verificar entidad Propietario existe",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Propietario' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### DOM-005: Gestión de Pagos
```json
{
  "id": "DOM-005",
  "categoria": "Dominio",
  "descripcion": "Verificar clase o servicio de pagos",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Pago\\|PagoService' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### DOM-006: Sistema de Ajustes
```json
{
  "id": "DOM-006",
  "categoria": "Dominio",
  "descripcion": "Verificar implementación de ajustes de renta",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'ajuste\\|Ajuste' --include='*.py' . | wc -l",
  "puntaje": 3,
  "threshold": 5,
  "peso": "medio"
}
```

---

## Sección 2: Verificaciones Dinámicas (Ejecución)

### 2.1 Ejecución Exitosa

#### EXEC-001: Ejecutar main.py Sin Errores
```json
{
  "id": "EXEC-001",
  "categoria": "Ejecucion",
  "descripcion": "Verificar que main.py ejecuta sin errores",
  "tipo": "dinamica",
  "metodo": "python",
  "comando": "timeout 30 python main.py",
  "puntaje": 10,
  "threshold": 0,
  "peso": "critico",
  "validacion": "return_code == 0"
}
```

---

#### EXEC-002: Mensaje de Éxito Final
```json
{
  "id": "EXEC-002",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje EJEMPLO COMPLETADO EXITOSAMENTE",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep 'EJEMPLO COMPLETADO EXITOSAMENTE'",
  "puntaje": 5,
  "threshold": 1,
  "peso": "critico"
}
```

---

#### EXEC-003: No Excepciones No Manejadas
```json
{
  "id": "EXEC-003",
  "categoria": "Ejecucion",
  "descripcion": "Verificar ausencia de tracebacks",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'traceback\\|error:' | wc -l",
  "puntaje": 5,
  "threshold": 0,
  "peso": "alto",
  "inverted": true
}
```

---

### 2.2 Patrones en Acción

#### EXEC-004: Patrón Singleton Demostrado
```json
{
  "id": "EXEC-004",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Singleton en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'singleton'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

---

#### EXEC-005: Patrón Factory Demostrado
```json
{
  "id": "EXEC-005",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Factory en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'factory'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

---

#### EXEC-006: Patrón Observer Demostrado
```json
{
  "id": "EXEC-006",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Observer en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'observer'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

---

#### EXEC-007: Patrón Strategy Demostrado
```json
{
  "id": "EXEC-007",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Strategy en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'strategy'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

---

### 2.3 Funcionalidad Inmobiliaria

#### EXEC-008: Registro de Propiedades Funcional
```json
{
  "id": "EXEC-008",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar mensaje de registro de propiedades",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'propiedad\\|casa\\|departamento'",
  "puntaje": 3,
  "threshold": 3,
  "peso": "alto"
}
```

---

#### EXEC-009: Contratos Funcional
```json
{
  "id": "EXEC-009",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar mensaje de contratos",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'contrato\\|alquiler'",
  "puntaje": 3,
  "threshold": 2,
  "peso": "alto"
}
```

---

#### EXEC-010: Persistencia Funcional
```json
{
  "id": "EXEC-010",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar archivo persistido existe",
  "tipo": "dinamica",
  "metodo": "filesystem",
  "comando": "timeout 30 python main.py && find ./data -name '*.dat' -type f",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

---

#### EXEC-011: Monitoreo Automatizado
```json
{
  "id": "EXEC-011",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar sistema de monitoreo activo",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'monitor\\|alerta\\|vencimiento'",
  "puntaje": 4,
  "threshold": 2,
  "peso": "alto"
}
```

---

#### EXEC-012: Gestión de Pagos
```json
{
  "id": "EXEC-012",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar registro de pagos",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'pago\\|monto'",
  "puntaje": 3,
  "threshold": 2,
  "peso": "medio"
}
```

---

## Sección 3: Métricas de Código

### 3.1 Complejidad Ciclomática

#### METR-001: Complejidad Promedio Baja
```json
{
  "id": "METR-001",
  "categoria": "Metricas",
  "descripcion": "Verificar complejidad ciclomática promedio < 10",
  "tipo": "estatica",
  "metodo": "radon",
  "comando": "radon cc . -a -s",
  "puntaje": 3,
  "threshold": 10,
  "peso": "bajo",
  "requires_tool": "radon"
}
```

**Instalación**: `pip install radon`

---

### 3.2 Líneas de Código

#### METR-002: Total de Líneas de Código
```json
{
  "id": "METR-002",
  "categoria": "Metricas",
  "descripcion": "Contar líneas de código Python",
  "tipo": "estatica",
  "metodo": "cloc",
  "comando": "find . -name '*.py' -not -path './.venv/*' -exec wc -l {} + | tail -1",
  "puntaje": 0,
  "threshold": 500,
  "peso": "informativo"
}
```

**Nota**: `puntaje: 0` indica que es solo informativo

---

### 3.3 Duplicación de Código

#### METR-003: Código Duplicado
```json
{
  "id": "METR-003",
  "categoria": "Metricas",
  "descripcion": "Detectar código duplicado con PMD CPD",
  "tipo": "estatica",
  "metodo": "cpd",
  "comando": "pmd cpd --minimum-tokens 50 --language python --files .",
  "puntaje": 3,
  "threshold": 5,
  "peso": "bajo",
  "requires_tool": "pmd",
  "inverted": true
}
```

**Instalación**: Descargar PMD desde https://pmd.github.io/

---

## Sección 4: Tests (Opcional)

### 4.1 Tests Unitarios

#### TEST-001: Tests Existen
```json
{
  "id": "TEST-001",
  "categoria": "Tests",
  "descripcion": "Verificar archivos de tests",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name 'test_*.py' -o -name '*_test.py' | wc -l",
  "puntaje": 5,
  "threshold": 1,
  "peso": "bonus"
}
```

---

#### TEST-002: Coverage > 70%
```json
{
  "id": "TEST-002",
  "categoria": "Tests",
  "descripcion": "Verificar cobertura de tests",
  "tipo": "dinamica",
  "metodo": "pytest",
  "comando": "pytest --cov=. --cov-report=term-missing | grep 'TOTAL' | awk '{print $4}'",
  "puntaje": 10,
  "threshold": 70,
  "peso": "bonus",
  "requires_tool": "pytest-cov"
}
```

---

## Workflow de n8n - Estructura Completa

### Nodo 1: Inicializar Evaluación

```json
{
  "nodes": [
    {
      "name": "Inicializar",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "values": {
          "string": [
            {
              "name": "proyecto_path",
              "value": "/path/to/proyecto"
            },
            {
              "name": "puntaje_total",
              "value": 0
            },
            {
              "name": "criterios_pasados",
              "value": 0
            },
            {
              "name": "criterios_fallados",
              "value": 0
            }
          ]
        }
      }
    }
  ]
}
```

---

### Nodo 2: Ejecutar Verificaciones Estáticas

```json
{
  "name": "Verificaciones Estaticas",
  "type": "n8n-nodes-base.executeCommand",
  "parameters": {
    "command": "={{ $json.comando }}",
    "cwd": "={{ $json.proyecto_path }}"
  }
}
```

**Input esperado**: Array de criterios estáticos (SING-*, FACT-*, etc.)

---

### Nodo 3: Ejecutar Verificaciones Dinámicas

```json
{
  "name": "Verificaciones Dinamicas",
  "type": "n8n-nodes-base.executeCommand",
  "parameters": {
    "command": "python main.py",
    "cwd": "={{ $json.proyecto_path }}",
    "timeout": 30000
  }
}
```

---

### Nodo 4: Evaluar Criterios

```json
{
  "name": "Evaluar Criterio",
  "type": "n8n-nodes-base.function",
  "parameters": {
    "functionCode": "const output = $input.all();\nconst criterio = $json;\nconst resultado = output[0].json.stdout;\nconst coincidencias = (resultado.match(/\\n/g) || []).length;\n\nif (criterio.inverted) {\n  criterio.pasado = coincidencias <= criterio.threshold;\n} else {\n  criterio.pasado = coincidencias >= criterio.threshold;\n}\n\ncriterio.puntaje_obtenido = criterio.pasado ? criterio.puntaje : 0;\n\nreturn criterio;"
  }
}
```

---

### Nodo 5: Calcular Puntaje Total

```json
{
  "name": "Calcular Total",
  "type": "n8n-nodes-base.aggregate",
  "parameters": {
    "aggregate": "aggregateAllItemData",
    "fieldsToAggregate": {
      "fieldToAggregate": [
        {
          "fieldToAggregate": "puntaje_obtenido",
          "renameField": false,
          "operation": "sum",
          "outputFieldName": "puntaje_total"
        }
      ]
    }
  }
}
```

---

### Nodo 6: Generar Reporte

```json
{
  "name": "Generar Reporte",
  "type": "n8n-nodes-base.function",
  "parameters": {
    "functionCode": "const puntaje = $json.puntaje_total;\nconst criterios = $input.all();\n\nconst pasados = criterios.filter(c => c.json.pasado).length;\nconst fallados = criterios.filter(c => !c.json.pasado).length;\n\nconst porcentaje = (puntaje / 270) * 100;\n\nlet calificacion = 'Insuficiente';\nif (porcentaje >= 90) calificacion = 'Excelente';\nelse if (porcentaje >= 80) calificacion = 'Muy Bueno';\nelse if (porcentaje >= 70) calificacion = 'Bueno';\nelse if (porcentaje >= 60) calificacion = 'Suficiente';\n\nreturn {\n  puntaje_total: puntaje,\n  puntaje_maximo: 270,\n  porcentaje: porcentaje.toFixed(2),\n  calificacion: calificacion,\n  criterios_pasados: pasados,\n  criterios_fallados: fallados,\n  aprobado: porcentaje >= 70\n};"
  }
}
```

---

### Nodo 7: Enviar Notificación

```json
{
  "name": "Enviar Email",
  "type": "n8n-nodes-base.emailSend",
  "parameters": {
    "fromEmail": "evaluacion@inmobiliaria.com",
    "toEmail": "={{ $json.estudiante_email }}",
    "subject": "Resultado Evaluación - {{ $json.calificacion }}",
    "text": "Puntaje: {{ $json.puntaje_total }}/270 ({{ $json.porcentaje }}%)\nCalificación: {{ $json.calificacion }}\nCriterios pasados: {{ $json.criterios_pasados }}\nCriterios fallados: {{ $json.criterios_fallados }}"
  }
}
```

---

## Archivo de Configuración Completa (JSON)

```json
{
  "evaluacion": {
    "version": "1.0.0",
    "puntaje_maximo": 270,
    "umbral_aprobacion": 189,
    "criterios": [
      {
        "id": "SING-001",
        "categoria": "Singleton",
        "tipo": "estatica",
        "comando": "grep -rn '_instance = None' --include='*.py' .",
        "puntaje": 2,
        "threshold": 1,
        "peso": "alto"
      },
      {
        "id": "SING-002",
        "categoria": "Singleton",
        "tipo": "estatica",
        "comando": "grep -rn 'def __new__' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "FACT-001",
        "categoria": "Factory",
        "tipo": "estatica",
        "comando": "grep -rn '@staticmethod' --include='*factory*.py' .",
        "puntaje": 3,
        "threshold": 2,
        "peso": "critico"
      },
      {
        "id": "OBSR-001",
        "categoria": "Observer",
        "tipo": "estatica",
        "comando": "grep -rn 'class Observable' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "STRT-001",
        "categoria": "Strategy",
        "tipo": "estatica",
        "comando": "grep -rn 'class.*Strategy.*ABC' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "DOM-001",
        "categoria": "Dominio",
        "tipo": "estatica",
        "comando": "grep -rn 'class Casa\\|class Departamento\\|class Finca' --include='*.py' .",
        "puntaje": 3,
        "threshold": 3,
        "peso": "critico"
      },
      {
        "id": "EXEC-001",
        "categoria": "Ejecucion",
        "tipo": "dinamica",
        "comando": "timeout 30 python main.py",
        "puntaje": 10,
        "threshold": 0,
        "peso": "critico",
        "validacion": "return_code == 0"
      },
      {
        "id": "EXEC-008",
        "categoria": "Funcionalidad",
        "tipo": "dinamica",
        "comando": "timeout 30 python main.py 2>&1 | grep -i 'propiedad\\|casa\\|departamento'",
        "puntaje": 3,
        "threshold": 3,
        "peso": "alto"
      },
      {
        "id": "QUAL-001",
        "categoria": "Calidad",
        "tipo": "estatica",
        "comando": "find . -name 'constantes.py' -type f",
        "puntaje": 3,
        "threshold": 1,
        "peso": "alto"
      }
    ]
  }
}
```

---

## Script Python Helper para n8n

### evaluador_automatico.py

```python
#!/usr/bin/env python3
"""
Script helper para evaluación automatizada de sistemas inmobiliarios.
Uso: python evaluador_automatico.py --proyecto /path/to/proyecto --config config.json
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

class EvaluadorAutomatico:
    def __init__(self, proyecto_path: str, config_path: str):
        self.proyecto_path = Path(proyecto_path)
        self.config = self._cargar_config(config_path)
        self.resultados = []

    def _cargar_config(self, config_path: str) -> Dict:
        with open(config_path, 'r') as f:
            return json.load(f)

    def ejecutar_comando(self, comando: str) -> Dict[str, Any]:
        """Ejecuta comando y retorna resultado."""
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                cwd=self.proyecto_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                'exitcode': resultado.returncode,
                'stdout': resultado.stdout,
                'stderr': resultado.stderr,
                'exito': resultado.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                'exitcode': -1,
                'stdout': '',
                'stderr': 'Timeout',
                'exito': False
            }

    def evaluar_criterio(self, criterio: Dict) -> Dict:
        """Evalua un criterio individual."""
        resultado_cmd = self.ejecutar_comando(criterio['comando'])

        # Contar coincidencias
        coincidencias = resultado_cmd['stdout'].count('\n')

        # Evaluar según threshold
        inverted = criterio.get('inverted', False)
        if inverted:
            pasado = coincidencias <= criterio['threshold']
        else:
            pasado = coincidencias >= criterio['threshold']

        return {
            'id': criterio['id'],
            'categoria': criterio['categoria'],
            'pasado': pasado,
            'coincidencias': coincidencias,
            'threshold': criterio['threshold'],
            'puntaje_max': criterio['puntaje'],
            'puntaje_obtenido': criterio['puntaje'] if pasado else 0,
            'peso': criterio['peso'],
            'output': resultado_cmd['stdout'][:500]  # Primeros 500 chars
        }

    def evaluar_todos(self) -> Dict:
        """Evalua todos los criterios."""
        for criterio in self.config['evaluacion']['criterios']:
            resultado = self.evaluar_criterio(criterio)
            self.resultados.append(resultado)

        # Calcular totales
        puntaje_total = sum(r['puntaje_obtenido'] for r in self.resultados)
        puntaje_maximo = self.config['evaluacion']['puntaje_maximo']
        porcentaje = (puntaje_total / puntaje_maximo) * 100

        # Determinar calificación
        if porcentaje >= 90:
            calificacion = 'Excelente'
        elif porcentaje >= 80:
            calificacion = 'Muy Bueno'
        elif porcentaje >= 70:
            calificacion = 'Bueno'
        elif porcentaje >= 60:
            calificacion = 'Suficiente'
        else:
            calificacion = 'Insuficiente'

        return {
            'puntaje_total': puntaje_total,
            'puntaje_maximo': puntaje_maximo,
            'porcentaje': round(porcentaje, 2),
            'calificacion': calificacion,
            'aprobado': porcentaje >= 70,
            'criterios_pasados': sum(1 for r in self.resultados if r['pasado']),
            'criterios_fallados': sum(1 for r in self.resultados if not r['pasado']),
            'resultados': self.resultados
        }

    def generar_reporte_json(self, output_path: str):
        """Genera reporte en formato JSON."""
        resumen = self.evaluar_todos()
        with open(output_path, 'w') as f:
            json.dump(resumen, f, indent=2)

    def generar_reporte_markdown(self, output_path: str):
        """Genera reporte en formato Markdown."""
        resumen = self.evaluar_todos()

        markdown = f"""# Reporte de Evaluación Automatizada - Sistema Inmobiliario

**Proyecto**: {self.proyecto_path.name}
**Fecha**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumen

- **Puntaje Total**: {resumen['puntaje_total']}/{resumen['puntaje_maximo']}
- **Porcentaje**: {resumen['porcentaje']}%
- **Calificación**: {resumen['calificacion']}
- **Estado**: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}

## Detalles

| Criterio | Categoría | Pasado | Puntaje | Peso |
|----------|-----------|--------|---------|------|
"""
        for r in self.resultados:
            estado = '✓' if r['pasado'] else '✗'
            markdown += f"| {r['id']} | {r['categoria']} | {estado} | {r['puntaje_obtenido']}/{r['puntaje_max']} | {r['peso']} |\n"

        with open(output_path, 'w') as f:
            f.write(markdown)


if __name__ == '__main__':
    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser(description='Evaluador automático de proyectos inmobiliarios')
    parser.add_argument('--proyecto', required=True, help='Path al proyecto')
    parser.add_argument('--config', required=True, help='Path al archivo de configuración')
    parser.add_argument('--output-json', help='Path para reporte JSON')
    parser.add_argument('--output-md', help='Path para reporte Markdown')

    args = parser.parse_args()

    evaluador = EvaluadorAutomatico(args.proyecto, args.config)

    if args.output_json:
        evaluador.generar_reporte_json(args.output_json)
        print(f"Reporte JSON generado: {args.output_json}")

    if args.output_md:
        evaluador.generar_reporte_markdown(args.output_md)
        print(f"Reporte Markdown generado: {args.output_md}")

    # Imprimir resumen en consola
    resumen = evaluador.evaluar_todos()
    print(f"\n=== RESUMEN ===")
    print(f"Puntaje: {resumen['puntaje_total']}/{resumen['puntaje_maximo']} ({resumen['porcentaje']}%)")
    print(f"Calificación: {resumen['calificacion']}")
    print(f"Estado: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}")

    sys.exit(0 if resumen['aprobado'] else 1)
```

---

## Uso del Sistema de Evaluación

### 1. Preparar Configuración

Crear `config.json` con criterios deseados (usar JSON de sección anterior).

### 2. Ejecutar Evaluación Local

```bash
python evaluador_automatico.py \
  --proyecto /path/to/PythonInmobiliaria \
  --config config.json \
  --output-json resultado.json \
  --output-md resultado.md
```

### 3. Integrar con n8n

1. Importar workflow de n8n (JSON proporcionado)
2. Configurar nodos con paths correctos
3. Conectar con sistema de notificaciones (email, Slack, etc.)
4. Ejecutar workflow manualmente o mediante webhook

### 4. Automatizar con Git Hooks

```bash
#!/bin/bash
# .git/hooks/pre-push

echo "Ejecutando evaluación automática..."
python evaluador_automatico.py \
  --proyecto . \
  --config .rubrica/config.json \
  --output-json .rubrica/ultimo_resultado.json

if [ $? -eq 0 ]; then
  echo "Evaluación APROBADA - Permitiendo push"
  exit 0
else
  echo "Evaluación FALLIDA - Bloqueando push"
  exit 1
fi
```

---

## Pesos de Criterios

| Peso | Valor Numérico | Uso |
|------|----------------|-----|
| **critico** | 1.5x | Criterios fundamentales (patrones principales, dominio) |
| **alto** | 1.2x | Criterios importantes (calidad, estructura, funcionalidad) |
| **medio** | 1.0x | Criterios deseables (documentación, type hints) |
| **bajo** | 0.8x | Criterios opcionales (métricas, extras) |
| **bonus** | 0.5x | Criterios adicionales (tests, CI/CD) |

---

## Distribución de Puntaje por Categoría

| Categoría | Puntaje Máximo | Porcentaje |
|-----------|----------------|------------|
| Singleton | 10 | 3.7% |
| Factory Method | 10 | 3.7% |
| Observer | 13 | 4.8% |
| Strategy | 10 | 3.7% |
| Dominio Inmobiliario | 13 | 4.8% |
| Calidad de Código | 12 | 4.4% |
| Estructura | 8 | 3.0% |
| Ejecución | 23 | 8.5% |
| Funcionalidad | 16 | 5.9% |
| Métricas | 6 | 2.2% |
| Tests (Bonus) | 15 | 5.6% |
| **TOTAL** | **270** | **100%** |

---

## Conclusiones

Este sistema de evaluación automatizada permite:

1. **Evaluación objetiva**: Criterios verificables automáticamente
2. **Escalabilidad**: Evaluar múltiples proyectos simultáneamente
3. **Consistencia**: Mismos criterios para todos los proyectos
4. **Rapidez**: Evaluación completa en < 1 minuto
5. **Trazabilidad**: Reportes detallados en JSON/Markdown
6. **Integración**: Compatible con n8n, CI/CD, Git hooks
7. **Dominio específico**: Validaciones adaptadas al contexto inmobiliario

---

**Versión**: 1.0.0
**Última Actualización**: Noviembre 2025
**Compatible con**: n8n v1.0+, Python 3.13+