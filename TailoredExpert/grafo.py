class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def cargar_datos(self, archivo_json):
        import json
        with open(archivo_json, 'r') as f:
            datos = json.load(f)
            self.nodos = datos.get('nodos', {})
            self.aristas = datos.get('aristas', {})

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.aristas:
            self.aristas[nodo1] = {}
        self.aristas[nodo1][nodo2] = peso

    def obtener_vecinos(self, nodo):
        return self.aristas.get(nodo, {})

    def consultar_nodo(self, nodo):
        return self.nodos.get(nodo, None)

    def obtener_aristas(self):
        return self.aristas

    def obtener_nodos(self):
        return self.nodos.keys()