# src/formatters.py
from pathlib import Path
import json
from typing import Dict, Any

class Formateador:
    def __init__(self, idioma: str = 'es'):
        self.plantillas = self._cargar_plantillas(idioma)

    def _cargar_plantillas(self, idioma: str) -> Dict:
        ruta = Path(f'kb/templates/{idioma}.json')
        return json.loads(ruta.read_text(encoding='utf-8'))

    def formatear(self, tipo: str, datos: Dict[str, Any]) -> str:
        try:
            plantilla = self.plantillas['respuestas'][tipo]['exito']
            return plantilla.format(**datos)
        except Exception:
            return self.plantillas['errores']['general']