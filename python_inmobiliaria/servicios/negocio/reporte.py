"""Servicio de reportes."""
class Reporte:
    """Servicio para generacion de reportes."""
    def generar_reporte_simple(self, titulo: str, contenido: str) -> None:
        print()
        print("=" * 70)
        print(f"  {titulo}")
        print("=" * 70)
        print(contenido)
        print("=" * 70)
