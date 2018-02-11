from datetime import datetime
import json


class Persona:

    def __init__(self, nombre, edad, estado_civil):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.idn = next(Persona.gen)

    def get_id():
        i = 1
        while True:
            yield i
            i += 1

    gen = get_id()


class PersonaEncoder(json.JSONEncoder):

    def default(self, obj):
        # Creamos una serialización personalizada para el
        # el tipo de objeto Persona

        if isinstance(obj, Persona):
            return {'Persona_id': obj.idn,
                    'nombre': obj.nombre,
                    'edad': obj.edad,
                    'estado_civil': obj.estado_civil,
                    'fecha_nac': datetime.now().year - obj.edad}

        # Mantenemos la serialización por defecto para
        # cualquier otro tipo de objeto
        return super().default(obj)


p1 = Persona("Juan", 37, "Soltero")
p2 = Persona("Jorge", 33, "Casado")
p3 = Persona("Pedro", 24, "Soltero")

print("Serialización default:\n")

# con esto serializamos directamente usando el default
json_string = json.dumps(p1.__dict__)
print(json_string)

# Ahora serializamos usando el método personalizado
print("\nSerialización personalizada:\n")
json_string = json.dumps(p1, cls=PersonaEncoder)
print(json_string)

json_string = json.dumps(p2, cls=PersonaEncoder)
print(json_string)

json_string = json.dumps(p3, cls=PersonaEncoder)
print(json_string)
