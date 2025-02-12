# Orquestador principal del agente
from grafo import Grafo
import os

def main(ruta_personalizada: str = None):
    """
    Punto de entrada principal.
    Preparado para personalización y extensión.
    """
    grafo = Grafo(kb_path=ruta_personalizada or 'kb')
    return grafo

if __name__ == "__main__":
    g = main()