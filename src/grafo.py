# src/grafo.py
from typing import Dict, Any, List, Optional, Set
from .response import Response

class Grafo:
    def __init__(self):
        self.nodos: Dict[str, Dict[str, Any]] = {}
        self.conexiones: Dict[str, Dict[str, float]] = {}
        self.response = Response()

    def agregar_nodo(self, id: str, datos: Dict[str, Any]) -> str:
        """Agrega un nuevo nodo al grafo"""
        try:
            if id in self.nodos:
                return self.response.get('error', {
                    'mensaje': 'El nodo ya existe'
                })
            self.nodos[id] = datos
            return self.response.get('nodo', {
                'resultado': f'Nodo {id} agregado correctamente'
            })
        except Exception as e:
            return self.response.get('error', {
                'mensaje': str(e)
            })

    def conectar(self, origen: str, destino: str, peso: float = 1.0) -> str:
        """Crea una conexión entre dos nodos"""
        try:
            if origen not in self.nodos or destino not in self.nodos:
                return self.response.get('error', {
                    'mensaje': 'Nodos no encontrados'
                })
            
            if origen not in self.conexiones:
                self.conexiones[origen] = {}
            
            self.conexiones[origen][destino] = peso
            return self.response.get('conexion', {
                'resultado': f'Conexión {origen}->{destino} creada'
            })
        except Exception as e:
            return self.response.get('error', {
                'mensaje': str(e)
            })

    def obtener_nodo(self, id: str) -> Optional[Dict[str, Any]]:
        """Obtiene la información de un nodo específico"""
        return self.nodos.get(id)

    def obtener_conexiones(self, id: str) -> Dict[str, float]:
        """Obtiene todas las conexiones de un nodo"""
        return self.conexiones.get(id, {})

    def eliminar_nodo(self, id: str) -> str:
        """Elimina un nodo y sus conexiones"""
        try:
            if id not in self.nodos:
                return self.response.get('error', {
                    'mensaje': 'Nodo no encontrado'
                })
            
            # Eliminar el nodo
            del self.nodos[id]
            
            # Eliminar conexiones salientes
            if id in self.conexiones:
                del self.conexiones[id]
            
            # Eliminar conexiones entrantes
            for origen in self.conexiones:
                if id in self.conexiones[origen]:
                    del self.conexiones[origen][id]
            
            return self.response.get('nodo', {
                'resultado': f'Nodo {id} eliminado correctamente'
            })
        except Exception as e:
            return self.response.get('error', {
                'mensaje': str(e)
            })

    def buscar_camino(self, origen: str, destino: str) -> List[str]:
        """Encuentra el camino más corto entre dos nodos usando BFS"""
        if origen not in self.nodos or destino not in self.nodos:
            return []
        
        visitados: Set[str] = set()
        cola = [(origen, [origen])]
        
        while cola:
            (vertice, camino) = cola.pop(0)
            for siguiente in self.conexiones.get(vertice, {}):
                if siguiente not in visitados:
                    if siguiente == destino:
                        return camino + [siguiente]
                    visitados.add(siguiente)
                    cola.append((siguiente, camino + [siguiente]))
        return []

    def obtener_info(self) -> Dict[str, Any]:
        """Retorna información general del grafo"""
        return {
            'total_nodos': len(self.nodos),
            'total_conexiones': sum(len(conexiones) for conexiones in self.conexiones.values()),
            'nodos': list(self.nodos.keys())
        }