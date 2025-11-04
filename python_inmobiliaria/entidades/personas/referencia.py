"""Entidad Referencia - Referencia personal."""
class Referencia:
    """Entidad Referencia - solo contiene datos."""
    def __init__(self, nombre: str, telefono: str, relacion: str):
        self._nombre = nombre
        self._telefono = telefono
        self._relacion = relacion
    def get_nombre(self) -> str:
        return self._nombre
    def get_telefono(self) -> str:
        return self._telefono
    def get_relacion(self) -> str:
        return self._relacion
