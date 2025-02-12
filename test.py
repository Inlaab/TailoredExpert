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
                # Solo agregamos el nodo una vez
                resultados.append({
                    'nivel': nivel,
                    'ruta': nueva_ruta,
                    'tipo': type(value).__name__,
                    'contenido': value if not isinstance(value, (dict, list)) else None,
                    'longitud': len(value) if isinstance(value, (dict, list)) else None
                })
                # Recursión para estructuras anidadas
                if isinstance(value, (dict, list)):
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
                if isinstance(item, (dict, list)):
                    nueva_ruta = f"{ruta}[{i}]"
                    resultados.extend(self.analizar_estructura_completa(item, nivel + 1, nueva_ruta))
                else:
                    resultados.append({
                        'nivel': nivel + 1,
                        'ruta': f"{ruta}[{i}]",
                        'tipo': type(item).__name__,
                        'contenido': item,
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
        
        # Procesar archivos
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
                    
                    # Crear nodo
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
        
        # Procesar conexiones
        for archivo, estructura in self.estructura_total.items():
            nodo_actual = archivo.replace('.json', '')
            for item in estructura:
                if 'conexiones' in item['ruta']:
                    if isinstance(item['contenido'], str):
                        self.grafo.agregar_conexion(nodo_actual, item['contenido'])
                    elif isinstance(item['contenido'], list):
                        for conexion in item['contenido']:
                            if isinstance(conexion, str):
                                self.grafo.agregar_conexion(nodo_actual, conexion)
                
        return True

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
            if conexiones:
                print(f"Conectado a: {', '.join(conexiones)}")
            
            if 'stats' in info:
                stats = info['stats']
                print(f"Profundidad máxima: {stats['profundidad_max']}")
                print(f"Total elementos: {stats['total_elementos']}")
                print(f"Tipos encontrados: {', '.join(sorted(stats['tipos']))}")
                
                estadisticas['total_elementos'] += stats['total_elementos']
                estadisticas['max_profundidad'] = max(estadisticas['max_profundidad'], 
                                                    stats['profundidad_max'])
                estadisticas['tipos_encontrados'].update(stats['tipos'])
                estadisticas['total_conexiones'] += len(conexiones)
        
        print("\nEstadísticas Globales:")
        print(f"Total elementos procesados: {estadisticas['total_elementos']}")
        print(f"Profundidad máxima global: {estadisticas['max_profundidad']}")
        print(f"Tipos únicos encontrados: {', '.join(sorted(estadisticas['tipos_encontrados']))}")
        print(f"Total conexiones: {estadisticas['total_conexiones']}")

    def test_escalabilidad(self):
        """Test de rendimiento y escalabilidad con estructura compleja"""
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
        
        return tiempo_total < 10

    def reporte_final(self):
        """Genera reporte final detallado sin repeticiones"""
        print("\n=== Reporte Final ===")
        print(f"Timestamp: {datetime.now()}")
        
        # Estadísticas de archivos KB
        print("\nEstadísticas de KB:")
        archivos_procesados = set()
        
        for archivo, estructura in self.estructura_total.items():
            if archivo not in archivos_procesados:
                archivos_procesados.add(archivo)
                print(f"\n{archivo}:")
                print(f"  Elementos: {len(estructura)}")
                max_profundidad = max(item['nivel'] for item in estructura)
                print(f"  Profundidad máxima: {max_profundidad}")
                tipos = set(item['tipo'] for item in estructura)
                print(f"  Tipos de datos: {', '.join(sorted(tipos))}")
        
        # Estadísticas del grafo
        nodos = self.grafo.obtener_nodos()
        total_nodos = len(nodos)
        total_conexiones = sum(len(self.grafo.obtener_conexiones(nodo)) for nodo in nodos)
        
        print("\nEstadísticas del Grafo:")
        print(f"Total nodos: {total_nodos}")
        print(f"Total conexiones: {total_conexiones}")
        if total_nodos > 0:
            print(f"Promedio conexiones/nodo: {total_conexiones/total_nodos:.2f}")
        
        # Métricas del grafo
        densidad = 0
        if total_nodos > 1:
            densidad = (2.0 * total_conexiones) / (total_nodos * (total_nodos - 1))
        
        print("\nMétricas del Grafo:")
        print(f"Densidad: {densidad:.4f}")
        print(f"Conectividad: {'Alta' if densidad > 0.5 else 'Media' if densidad > 0.2 else 'Baja'}")
        
        # Análisis de estructura global
        print("\nAnálisis Global:")
        todos_tipos = set()
        max_prof_global = 0
        total_elementos = 0
        
        for estructura in self.estructura_total.values():
            todos_tipos.update(item['tipo'] for item in estructura)
            max_prof_global = max(max_prof_global, max(item['nivel'] for item in estructura))
            total_elementos += len(estructura)
        
        print(f"Total elementos únicos: {total_elementos}")
        print(f"Profundidad máxima global: {max_prof_global}")
        print(f"Tipos únicos encontrados: {', '.join(sorted(todos_tipos))}")
        
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