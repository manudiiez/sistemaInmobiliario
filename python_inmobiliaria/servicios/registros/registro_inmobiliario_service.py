"""Servicio para registros inmobiliarios."""
# Standard library
import os
import pickle
from typing import TYPE_CHECKING
# Local application
from python_inmobiliaria.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_inmobiliaria.excepciones.persistencia_exception import PersistenciaException, TipoOperacion
if TYPE_CHECKING:
    from python_inmobiliaria.entidades.registros.registro_inmobiliario import RegistroInmobiliario

class RegistroInmobiliarioService:
    """Servicio para registros inmobiliarios con persistencia."""
    def persistir(self, registro: 'RegistroInmobiliario') -> None:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        propietario = registro.get_propietario()
        tipo_propiedad = registro.get_propiedad().obtener_tipo()
        nombre_archivo = f"{propietario.replace(' ', '_')}_{tipo_propiedad}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        archivo = None
        try:
            archivo = open(ruta_completa, 'wb')
            pickle.dump(registro, archivo)
            print(f"Registro de {propietario} ({tipo_propiedad}) persistido exitosamente en {ruta_completa}")
        except Exception as e:
            raise PersistenciaException(tipo_operacion=TipoOperacion.ESCRITURA, nombre_archivo=ruta_completa, causa=str(e))
        finally:
            if archivo:
                archivo.close()
    @staticmethod
    def leer_registro(propietario: str, tipo_propiedad: str) -> 'RegistroInmobiliario':
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")
        nombre_archivo = f"{propietario.replace(' ', '_')}_{tipo_propiedad}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        if not os.path.exists(ruta_completa):
            raise PersistenciaException(tipo_operacion=TipoOperacion.LECTURA, nombre_archivo=ruta_completa, causa="Archivo no encontrado")
        archivo = None
        try:
            archivo = open(ruta_completa, 'rb')
            registro = pickle.load(archivo)
            print(f"Registro de {propietario} ({tipo_propiedad}) recuperado exitosamente desde {ruta_completa}")
            return registro
        except Exception as e:
            raise PersistenciaException(tipo_operacion=TipoOperacion.LECTURA, nombre_archivo=ruta_completa, causa=str(e))
        finally:
            if archivo:
                archivo.close()
    def mostrar_datos(self, registro: 'RegistroInmobiliario') -> None:
        print()
        print("REGISTRO INMOBILIARIO")
        print("=" * 50)
        print(f"ID Registro:  {registro.get_id_registro()}")
        print(f"Propietario:  {registro.get_propietario()}")
        print(f"Valor Fiscal: {registro.get_valor_fiscal()}")
        print(f"Direccion:    {registro.get_propiedad().get_direccion()}")
        print(f"Superficie:   {registro.get_propiedad().get_superficie()} m2")
        print(f"Monto mensual: ${registro.get_contrato().get_monto_mensual():,.2f}")
