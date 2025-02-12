import json
import os

class VerificadorRespuestas:
    def __init__(self):
        self.kb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kb')
        self.data = {}
        self.cargar_todos_datos()

    def cargar_todos_datos(self):
        for archivo in os.listdir(self.kb_path):
            if archivo.endswith('.json'):
                with open(os.path.join(self.kb_path, archivo), 'r', encoding='utf-8') as f:
                    self.data[archivo] = json.load(f)

    def buscar_en_kb(self, consulta):
        palabras_clave = consulta.lower().split()
        resultados = []
        
        def buscar_recursivo(datos, ruta=[]):
            if isinstance(datos, dict):
                for k, v in datos.items():
                    nueva_ruta = ruta + [k]
                    if any(palabra in str(k).lower() for palabra in palabras_clave):
                        resultados.append({"ruta": nueva_ruta, "valor": v})
                    if isinstance(v, (dict, list)):
                        buscar_recursivo(v, nueva_ruta)
                    elif any(palabra in str(v).lower() for palabra in palabras_clave):
                        resultados.append({"ruta": nueva_ruta, "valor": v})
            elif isinstance(datos, list):
                for i, item in enumerate(datos):
                    buscar_recursivo(item, ruta + [i])

        for archivo, contenido in self.data.items():
            buscar_recursivo(contenido, [archivo])
        
        return resultados

    def verificar_respuesta(self, consulta):
        resultados = self.buscar_en_kb(consulta)
        return {
            "status": "éxito" if resultados else "error",
            "mensaje": f"Se encontraron {len(resultados)} coincidencias" if resultados else "No se encontró información",
            "datos": resultados
        }