# main.py

from agente_ia import AgenteIA
from grafo import Grafo

def main():
    # Initialize the graph
    grafo = Grafo()
    grafo.cargar_datos('kb/conocimiento.json')  # Load knowledge from JSON

    # Initialize the AI agent
    agente = AgenteIA(grafo)

    print("Bienvenido al servicio de atención al cliente. ¿En qué puedo ayudarte hoy?")
    
    while True:
        consulta = input("Tú: ")
        if consulta.lower() in ['salir', 'exit']:
            print("Agente: Gracias por usar el servicio. ¡Hasta luego!")
            break
        
        respuesta = agente.interactuar(consulta)
        print(f"Agente: {respuesta}")

if __name__ == "__main__":
    main()