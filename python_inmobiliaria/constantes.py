"""
Constantes centralizadas del sistema.

Este modulo contiene todas las constantes utilizadas en el sistema
para evitar valores magicos en el codigo.
"""

# Constantes de propiedades - Casa
SUPERFICIE_MINIMA_CASA = 50.0
VALOR_BASE_CASA = 4000000.0
FACTOR_TERRENO = 1.2
TERRENO_BASE_CASA = 250.0
PLANTAS_BASE_CASA = 2

# Constantes de propiedades - Departamento
SUPERFICIE_MINIMA_DEPTO = 30.0
VALOR_BASE_DEPTO = 2500000.0
FACTOR_PISO = 0.05
PISO_BASE_DEPTO = 5
NUMERO_BASE_DEPTO = 1

# Constantes de propiedades - Finca
SUPERFICIE_MINIMA_FINCA = 10000.0
VALOR_BASE_HECTAREA = 800000.0
TIPO_SUELO_BASE = "productivo"

# Constantes de contratos
DURACION_MINIMA_MESES = 6
DURACION_MAXIMA_MESES = 36
DEPOSITO_GARANTIA_MESES = 2

# Constantes de ajustes
AJUSTE_INFLACION_ANUAL = 1.25
MESES_AJUSTE_CONTRATO = 12

# Constantes de monitoreo
INTERVALO_MONITOR_FECHA = 86400
INTERVALO_MONITOR_PAGO = 3600
DIAS_ALERTA_VENCIMIENTO = 30
INTERVALO_CONTROL_VENCIMIENTO = 86400

# Constantes de threading
THREAD_JOIN_TIMEOUT = 2.0

# Constantes de persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
