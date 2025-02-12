import os
import json
import time
from datetime import datetime
from src.grafo import Grafo

class TestGrafo:
    def __init__(self):
        self.grafo = Grafo()
        self.estructura_total = {}
        
    def analizar_estructura_completa(self, data, nivel=0, ruta=""):
        """Analiza recursivamente TODA la estructura del archivo KB"""
        resultados = []
        
        if isinstance(data, dict):
            for key, value in data.items():
                nueva_ruta = f"{ruta}.{key}" if ruta else key
                resultados.append({
                    'nivel': nivel,
                    'ruta': nueva_ruta,
                    'tipo': type(value).__name__,
                    'contenido': value if not isinstance(value, (dict, list)) else None,
                    'longitud': len(value) if isinstance(value, (dict, list)) else None
                })
                resultados.extend(self.analizar_estructura_completa(value, nivel + 1, nueva_ruta))
                
        elif isinstance(data, list):
            resultados.append({
                'nivel': nivel,
                'ruta': ruta,
                'tipo': 'list',
                'contenido': None,
                'longitud': len(data)
            })
            for i, item in enumerate(data):
                nueva_ruta = f"{ruta}[{i}]"
                resultados.extend(self.analizar_estructura_completa(item, nivel + 1, nueva_ruta))
                
        elif isinstance(data, (str, int, float, bool)):
            resultados.append({
                'nivel': nivel,
                'ruta': ruta,
                'tipo': type(data).__name__,
                'contenido': data,
                'longitud': None
            })
            
        return resultados

    def test_kb_contenido(self):
        """Test de carga y análisis completo de archivos KB"""
        print("\n=== Análisis Completo de KB ===")
        
        if not os.path.exists("kb"):
            print("Error: Directorio 'kb' no encontrado")
            return False
            
        archivos = [f for f in os.listdir("kb") if f.endswith('.json')]
        if not archivos:
            print("No se encontraron archivos JSON en kb/")
            return False
            
        print("\nAnálisis de archivos:")
        
        for archivo in archivos:
            try:
                with open(f"kb/{archivo}", 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"\n=== Análisis de {archivo} ===")
                    
                    estructura = self.analizar_estructura_completa(data)
                    self.estructura_total[archivo] = estructura
                    
                    # Mostrar estructura
                    for item in estructura:
                        indent = "  " * item['nivel']
                        contenido = f"= {item['contenido']}" if item['contenido'] is not None else ""
                        longitud = f"(items: {item['longitud']})" if item['longitud'] is not None else ""
                        print(f"{indent}├─ {item['ruta']} [{item['tipo']}] {longitud} {contenido}")
                    
                    # Crear nodo con información completa
                    nodo = archivo.replace('.json', '')
                    self.grafo.agregar_nodo(nodo, {
                        'data': data,
                        'estructura': estructura,
                        'stats': {
                            'profundidad_max': max(item['nivel'] for item in estructura),
                            'total_elementos': len(estructura),
                            'tipos': list(set(item['tipo'] for item in estructura))
                        }
                    })
                    print(f"\n✓ {archivo} procesado y agregado como nodo: {nodo}")
                    
            except Exception as e:
                print(f"✗ Error al procesar {archivo}: {str(e)}")
                
        return True

    def test_escalabilidad(self):
        """Test de rendimiento y escalabilidad con estructura completa"""
        print("\n=== Prueba de Escalabilidad ===")
        inicio = time.time()
        
        # Crear nodos de prueba con estructura compleja
        nodos_prueba = 1000
        for i in range(nodos_prueba):
            data_prueba = {
                "id": i,
                "timestamp": str(datetime.now()),
                "config": {
                    "nivel": i % 5,
                    "activo": True,
                    "parametros": {
                        "p1": i * 1.5,
                        "p2": f"valor_{i}",
                        "lista": [1, 2, {"sub": "dato"}]
                    }
                },
                "conexiones": [f"conn_{j}" for j in range(3)]
            }
            
            estructura = self.analizar_estructura_completa(data_prueba)
            self.grafo.agregar_nodo(f"test_node_{i}", {
                'data': data_prueba,
                'estructura': estructura,
                'stats': {
                    'profundidad_max': max(item['nivel'] for item in estructura),
                    'total_elementos': len(estructura),
                    'tipos': list(set(item['tipo'] for item in estructura))
                }
            })
            
            if i > 0:
                self.grafo.agregar_conexion(f"test_node_{i}", f"test_node_{i-1}")
        
        fin = time.time()
        tiempo_total = fin - inicio
        
        print(f"Tiempo de creación: {tiempo_total:.2f} segundos")
        print(f"Velocidad: {nodos_prueba/tiempo_total:.2f} nodos/segundo")
        print(f"Total nodos: {len(self.grafo.obtener_nodos())}")
        
        return tiempo_total < 10  # Test exitoso si tarda menos de 10 segundos

    def test_estructura(self):
        """Test de estructura y conexiones con análisis profundo"""
        print("\n=== Análisis Profundo de Estructura ===")
        
        nodos = self.grafo.obtener_nodos()
        estadisticas = {
            'total_elementos': 0,
            'max_profundidad': 0,
            'tipos_encontrados': set(),
            'total_conexiones': 0
        }
        
        for nodo in nodos:
            info = self.grafo.obtener_info_nodo(nodo)
            conexiones = self.grafo.obtener_conexiones(nodo)
            
            print(f"\nNodo: {nodo}")
            print(f"Conexiones: {len(conexiones)}")
            
            if 'stats' in info:
                stats = info['stats']
                print(f"Profundidad máxima: {stats['profundidad_max']}")
                print(f"Total elementos: {stats['total_elementos']}")
                print(f"Tipos encontrados: {', '.join(stats['tipos'])}")
                
                estadisticas['total_elementos'] += stats['total_elementos']
                estadisticas['max_profundidad'] = max(estadisticas['max_profundidad'], 
                                                    stats['profundidad_max'])
                estadisticas['tipos_encontrados'].update(stats['tipos'])
                estadisticas['total_conexiones'] += len(conexiones)
        
        print("\nEstadísticas Globales:")
        print(f"Total elementos procesados: {estadisticas['total_elementos']}")
        print(f"Profundidad máxima global: {estadisticas['max_profundidad']}")
        print(f"Tipos únicos encontrados: {', '.join(estadisticas['tipos_encontrados'])}")
        print(f"Total conexiones: {estadisticas['total_conexiones']}")

    def reporte_final(self):
        """Genera reporte final detallado"""
        print("\n=== Reporte Final ===")
        print(f"Timestamp: {datetime.now()}")
        
        # Estadísticas de archivos KB
        print("\nEstadísticas de KB:")
        for archivo, estructura in self.estructura_total.items():
            print(f"\n{archivo}:")
            print(f"  Elementos: {len(estructura)}")
            print(f"  Profundidad máxima: {max(item['nivel'] for item in estructura)}")
            tipos = set(item['tipo'] for item in estructura)
            print(f"  Tipos de datos: {', '.join(tipos)}")
        
        # Estadísticas del grafo
        nodos = self.grafo.obtener_nodos()
        total_nodos = len(nodos)
        total_conexiones = sum(len(self.grafo.obtener_conexiones(nodo)) for nodo in nodos)
        
        print("\nEstadísticas del Grafo:")
        print(f"Total nodos: {total_nodos}")
        print(f"Total conexiones: {total_conexiones}")
        print(f"Promedio conexiones/nodo: {total_conexiones/total_nodos if total_nodos else 0:.2f}")
        
        print("\nEstado: " + ("OK" if total_conexiones > 0 else "Revisar conexiones"))

def main():
    print("=== Iniciando Suite de Pruebas ===")
    test = TestGrafo()
    
    # Ejecutar pruebas
    kb_ok = test.test_kb_contenido()
    if kb_ok:
        test.test_estructura()
        test.test_escalabilidad()
        test.reporte_final()
    else:
        print("Error en carga de KB. Pruebas canceladas.")

if __name__ == "__main__":
    main()