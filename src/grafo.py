import json
import os
from datetime import datetime
from pathlib import Path

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.ultima_actualizacion = datetime.now()

    def cargar_desde_kb(self):
        """Carga los datos desde los archivos JSON en la carpeta kb"""
        kb_path = Path("kb")
        print("\nArchivos en kb:")
        
        for archivo in kb_path.glob("*.json"):
            try:
                with open(archivo, 'r') as f:
                    datos = json.load(f)
                    
                if isinstance(datos, dict) and 'nodo' in datos:
                    print(f"✓ {archivo.name}: {datos['nodo']}")
                    self.agregar_nodo(datos['nodo'], {
                        'tipo': datos.get('tipo'),
                        'descripcion': datos.get('descripcion', ''),
                        'propiedades': datos.get('propiedades', {})
                    })
                    
                    # Procesar conexiones
                    for conexion in datos.get('conexiones', []):
                        if isinstance(conexion, str):
                            self.agregar_conexion(datos['nodo'], conexion)
                else:
                    print(f"Ignorando conexión inválida en {archivo}: {datos}")
                    
            except json.JSONDecodeError:
                print(f"Error al leer {archivo}: formato JSON inválido")
            except Exception as e:
                print(f"Error procesando {archivo}: {str(e)}")

    def agregar_nodo(self, nombre, metadata=None):
        """Agrega un nuevo nodo al grafo"""
        if metadata is None:
            metadata = {}
        if nombre not in self.nodos:
            self.nodos[nombre] = {
                'metadata': metadata,
                'conexiones': []
            }
        self.ultima_actualizacion = datetime.now()
        return self.nodos[nombre]

    def agregar_conexion(self, origen, destino):
        """Agrega una conexión entre dos nodos"""
        if origen in self.nodos and destino in self.nodos:
            if destino not in self.nodos[origen]['conexiones']:
                self.nodos[origen]['conexiones'].append(destino)
            if origen not in self.nodos[destino]['conexiones']:
                self.nodos[destino]['conexiones'].append(origen)
            self.ultima_actualizacion = datetime.now()

    def obtener_nodos(self):
        """Retorna la lista de nombres de nodos"""
        return list(self.nodos.keys())

    def obtener_conexiones(self, nodo):
        """Retorna las conexiones de un nodo"""
        return self.nodos.get(nodo, {}).get('conexiones', [])

    def obtener_info_nodo(self, nodo):
        """Retorna la metadata de un nodo"""
        return self.nodos.get(nodo, {}).get('metadata', {})

    def obtener_estadisticas(self):
        """Retorna estadísticas del grafo"""
        return {
            'nodos': len(self.nodos),
            'conexiones': sum(len(n['conexiones']) for n in self.nodos.values()) // 2,
            'ultima_actualizacion': self.ultima_actualizacion
        }