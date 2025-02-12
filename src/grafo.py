# grafo.py
import json
import os
from datetime import datetime

class Grafo:
    def __init__(self, kb_path='kb'):
        self.vertices = {}
        self.aristas = []
        self.kb_path = kb_path
        self.ultima_actualizacion = None
        self.archivos_procesados = {}
        self.cargar_conocimiento()

    def agregar_vertice(self, id, datos=None):
        if id not in self.vertices:
            self.vertices[id] = {
                'datos': datos,
                'conexiones': set()
            }
            return True
        return False

    def agregar_arista(self, origen, destino, peso=1):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['conexiones'].add(destino)
            self.aristas.append((origen, destino, peso))
            return True
        return False

    def cargar_conocimiento(self):
        """Carga inicial y actualización de conocimiento desde /kb"""
        archivos = os.listdir(self.kb_path)
        print(f"Archivos encontrados: {archivos}")  # Debug
        for archivo in archivos:
            if archivo.endswith('.json'):
                ruta_completa = os.path.join(self.kb_path, archivo)
                print(f"Procesando: {ruta_completa}")  # Debug
                self._procesar_archivo(ruta_completa)
        self.ultima_actualizacion = datetime.now()

    def _procesar_archivo(self, ruta):
        """Procesa un archivo JSON y actualiza el grafo"""
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self._actualizar_grafo(datos)
                self.archivos_procesados[ruta] = os.path.getmtime(ruta)
        except Exception as e:
            print(f"Error procesando {ruta}: {e}")

    def _actualizar_grafo(self, datos):
        """Actualiza el grafo con nuevos datos"""
        if 'concepto' in datos:
            self.agregar_vertice(datos['concepto'])
            for relacion in datos.get('relaciones', []):
                self.agregar_vertice(relacion)
                self.agregar_arista(datos['concepto'], relacion)

    def obtener_conexiones(self, vertice):
        return list(self.vertices.get(vertice, {}).get('conexiones', set()))

    def existe_camino(self, origen, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if origen == destino:
            return True
        visitados.add(origen)
        for vecino in self.vertices[origen]['conexiones']:
            if vecino not in visitados:
                if self.existe_camino(vecino, destino, visitados):
                    return True
        return False

    def mostrar_estado(self):
        print("\n=== Estado del Grafo ===")
        print(f"Nodos: {len(self.vertices)}")
        print(f"Conexiones: {len(self.aristas)}")
        print(f"Última actualización: {self.ultima_actualizacion}")
        print("=====================\n")

if __name__ == "__main__":
    grafo = Grafo()
    grafo.mostrar_estado()