from io import StringIO, BytesIO
import pickle
'''
file_in = StringIO('textó')
file_out = BytesIO()
print(file_in)
print(file_out)

char = file_in.read(1)
while char:
    file_out.write(char.encode('ascii', 'ignore'))
    char = file_in.read(1)

buffer_ = file_out.getvalue()
print(buffer_)


tupla = ('a', 1, 3, 'holi')
'''
# returns pickle representation of the object as a bytes object
serial = pickle.dumps(tupla)
print(serial)
print(type(serial))
print(pickle.loads(serial))

lista = [1, 2, 3, 4, 5]
with open('mi_lista', 'wb') as file:
    pickle.dump(lista, file)

with open('mi_lista', 'rb') as file:
    mi_lista = pickle.load(file)
    print(mi_lista)
    print(mi_lista[0])


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mensaje = 'No pasa nada'

    def __getstate__(self):
        nueva = self.__dict__.copy()
        nueva.update({'mensaje': 'Me estan serializando'})
        return nueva

    def __setstate__(self, state):
        print('Objecto recien des serializado')
        state.update({'nombre': state['nombre'] + ' deserializado'})
        self.__dict__ = state

m = Persona('Juan', 30)
print(m.__dict__)
serial = pickle.dumps(m)
m2 = pickle.loads(serial)

print(m.nombre)
print(m2.nombre)
print(m2.__dict__)
