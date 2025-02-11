class AgenteIA:
    def __init__(self, grafo):
        self.grafo = grafo

    def procesar_consulta(self, consulta):
        # Lógica para procesar la consulta en lenguaje natural
        pass

    def asignar_servicio(self, servicio, consultor):
        # Lógica para asignar un servicio a un consultor
        pass

    def calcular_distancia(self, nodo_a, nodo_b):
        # Lógica para calcular la distancia entre dos nodos
        pass

    def interactuar(self):
        while True:
            consulta = input("¿En qué puedo ayudarte? ")
            if consulta.lower() in ["salir", "exit"]:
                print("Gracias por usar el servicio. ¡Hasta luego!")
                break
            respuesta = self.procesar_consulta(consulta)
            print(respuesta)