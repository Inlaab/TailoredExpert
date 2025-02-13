# src/main.py
from grafo import GrafoBase
from typing import Dict, Optional

class AgenteBase:
    def __init__(self, kb_path: str = 'kb'):
        self.grafo = GrafoBase(kb_path)
        self.estado = {
            'activo': False,
            'errores': []
        }

    def inicializar(self) -> bool:
        """Inicialización con validación"""
        if self.grafo.cargar_kb():
            self.estado['activo'] = True
            return True
        self.estado['errores'] = self.grafo.obtener_estado()['errores_validacion']
        return False

    def consultar(self, id_nodo: str) -> Optional[Dict]:
        """Consulta segura de nodos"""
        if not self.estado['activo']:
            return None
        return self.grafo.nodos.get(id_nodo)

    def estado_actual(self) -> Dict:
        return {
            'agente': self.estado,
            'grafo': self.grafo.obtener_estado()
        }