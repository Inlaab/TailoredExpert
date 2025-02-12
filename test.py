from src.grafo import Grafo

# Inicializar grafo
g = Grafo()

# Verificar estado inicial
g.mostrar_estado()

# Verificar conexiones
print("\nConexiones desde 'Inteligencia Artificial':")
print(g.obtener_conexiones("Inteligencia Artificial"))

# Verificar camino
existe = g.existe_camino("Inteligencia Artificial", "Aprendizaje Supervisado")
print(f"\n¿Existe camino IA -> Aprendizaje Supervisado?: {existe}")