# IA Agent Template

Template base para crear agentes de IA basados en grafos. Diseñado para procesar y conectar conocimiento de forma dinámica mediante estructuras de grafos.

## Características
- Carga dinámica de conocimiento
- Procesamiento automático de JSON
- Sistema de conexiones flexible
- Escalable y personalizable

## Estructura
- `src/`: Código fuente del agente
  - `main.py`: Orquestador principal
  - `grafo.py`: Implementación base del grafo
- `kb/`: Base de conocimiento
  - `data_1.json`: Datos de ejemplo 1
  - `data_2.json`: Datos de ejemplo 2

## Requisitos
- Python 3.7+
- Archivos JSON válidos en kb/

## Uso
1. Clona este repositorio
2. Ejecuta `python setup.py` para crear la estructura
3. Modifica los archivos según tus necesidades

### Ejemplo básico
```python
from src.grafo import Grafo

# Inicializar grafo
grafo = Grafo()

# Ver estado
grafo.mostrar_estado()

# Plantilla Base para Agentes IA

Estructura base diseñada para crear agentes de IA escalables usando grafos de conocimiento.

## Características de la Plantilla

- **Estructura Simple**: Diseño minimalista y eficiente
- **Escalabilidad**: Preparada para crecer según necesidades
- **Independencia de LLM**: Compatible con cualquier modelo de lenguaje
- **Base de Conocimiento Flexible**: Estructura adaptable a diferentes formatos
- **Sistema de Grafos**: Implementación base para relaciones de conocimiento

## Estructura del Proyecto
{
    "ia-agent-template": {
        "src": {
            "main.py": "Punto de entrada y configuración",
            "grafo.py": "Motor de grafos"
        },
        "kb": {
            "*.json": "Archivos de conocimiento"
        },
        "setup.py": "Configuración del paquete",
        "README.md": "Documentación del proyecto"
    }
}

## Capacidades Base

1. **Gestión de Conocimiento**
   - Carga dinámica de datos
   - Validación de estructura
   - Gestión de relaciones

2. **Sistema de Grafos**
   - Creación y eliminación de nodos
   - Gestión de conexiones
   - Consultas básicas

3. **Extensibilidad**
   - Interfaz preparada para LLMs
   - Sistema de plugins
   - Adaptadores personalizables

## Requisitos
- Python 3.8+
- Estructura de archivos JSON definida

## Inicio Rápido
```python
from src.grafo import Grafo

# Inicializar agente
agente = Grafo()

# Configurar base de conocimiento
agente.cargar_kb("ruta/kb")

# Listo para implementar tu lógica