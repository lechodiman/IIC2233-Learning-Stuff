import json


class Persona:

    def __init__(self, nombre, edad, estado_civil):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.idn = next(Persona.gen)

    @classmethod
    def from_dict(cls, dict_obj):
        nombre = dict_obj['nombre']
        edad = dict_obj['edad']
        estado_civil = dict_obj['estado_civil']

        return cls(nombre, edad, estado_civil)

    def get_id():
        i = 1
        while True:
            yield i
            i += 1

    gen = get_id()


p = Persona('Juan', 35, 'Soltero')
json_string = json.dumps(p.__dict__)
print(json_string)
print(json.loads(json_string))

json_string = '{"nombre": "Jorge", "edad": 45}'
# print(json.loads(json_string))
print(type(json.loads(json_string)))

print(json.loads(json_string, parse_int=float))


json_string = '{"nombre":"Jorge","edad":34,"estado_civil": "casado", "puntaje" : 90.5}'
datos = json.loads(json_string, object_hook=lambda dict_obj: [tuple((i, j)) for i, j in dict_obj.items()])
print(datos)
