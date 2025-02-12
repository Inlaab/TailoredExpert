import os
import json

def create_directory_structure():
    directories = ['src', 'kb']
    for dir in directories:
        os.makedirs(dir, exist_ok=True)
    print("✓ Directorios creados")

def create_base_files():
    with open('src/main.py', 'w') as f:
        f.write('''# Orquestador principal del agente
def main():
    print("Agente IA iniciado")

if __name__ == "__main__":
    main()
''')
    print("✓ main.py creado")

    with open('src/grafo.py', 'w') as f:
        f.write('''# Implementación base del grafo
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []
''')
    print("✓ grafo.py creado")

def create_sample_data():
    sample_data_1 = {"tipo": "ejemplo", "datos": [1, 2, 3]}
    sample_data_2 = {"tipo": "conexiones", "datos": ["A", "B", "C"]}

    with open('kb/data_1.json', 'w') as f:
        json.dump(sample_data_1, f, indent=2)
    
    with open('kb/data_2.json', 'w') as f:
        json.dump(sample_data_2, f, indent=2)
    print("✓ Archivos JSON creados")

def create_readme():
    readme_content = '''# IA Agent Template

Template base para crear agentes de IA basados en grafos.

## Estructura
- `src/`: Código fuente del agente
  - `main.py`: Orquestador principal
  - `grafo.py`: Implementación base del grafo
- `kb/`: Base de conocimiento
  - `data_1.json`: Datos de ejemplo 1
  - `data_2.json`: Datos de ejemplo 2

## Uso
1. Clona este repositorio
2. Ejecuta `python setup.py` para crear la estructura
3. Modifica los archivos según tus necesidades

## Licencia
MIT'''

    try:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("✓ README.md creado")
    except Exception as e:
        print(f"Error creando README.md: {e}")

if __name__ == "__main__":
    print("Iniciando creación de estructura...")
    create_directory_structure()
    create_base_files()
    create_sample_data()
    create_readme()
    print("\n¡Estructura creada exitosamente!")