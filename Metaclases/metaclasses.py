'''
class CreadoraDeObjetos():
    pass


class MyClass(object):
    def __init__(self):
        self.x = 5

    def add(self):
        self.x += 1


def __init__(self):
    self.x = 5


def add(self):
    self.x += 1


def visualizar(o):
    print(o)


print(CreadoraDeObjetos)
CreadoraDeObjetos.peso = 80
CreadoraDeObjetos_Mirror = CreadoraDeObjetos
print(id(CreadoraDeObjetos_Mirror))
print(id(CreadoraDeObjetos))
print(CreadoraDeObjetos_Mirror.peso)


def crear_clase(name):
    if name == 'MiClase':
        class MiClase():
            pass
        return MiClase
    else:
        class CualquierClase:
            pass
        return CualquierClase


# c1 = crear_clase('MiClase')
# print(c1())
# c2 = crear_clase('Nose')
# print(c2())


my_class = MyClass()
NewClass = type("NewClass", (), {"__init__": __init__, "add": add})
nc = NewClass()
print(nc.x)

c2 = type('MiClase', (), {})

# this is a class
print(c2)

# this is an object of the class
print(c2())

Cuerpo = type('Cuerpo', (), {})
MiCuerpo = type('MiCuerpo', (Cuerpo, ), {})

print(issubclass(MiCuerpo, Cuerpo))
'''
# Creating Metaclasses


class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, diccionario):
        print('-----------------------------------')
        print("Creando la clase.. {} ".format(nombre))
        return super().__new__(meta, nombre, base_clases, diccionario)

    def __call__(cls, *args, **kwargs):
        print("__call__ of {}".format(str(cls)))
        print("__call__ *args = {}".format(str(args)))
        return super().__call__(*args, **kwargs)


class MetaFinal(type):
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, MetaFinal):
                raise TypeError('type {} is not an acceptable base type'.format(b.__name__))

        return super().__new__(cls, name, bases, classdict)


class MetaSoloUna(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class MetaPrueba1(type):
    def __call__(cls, *args, **kwargs):
        kw2 = dict(kwargs)
        kw2['nombre'] += ' Gonzales'
        kw2['edad'] += 1
        return super().__call__(*args, **kwargs), super().__call__(*args, **kw2)


class Prueba2(metaclass=MetaPrueba1):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre + str(self.edad)


class SoloUna(metaclass=MetaSoloUna):
    pass


class C(metaclass=MetaFinal):
    pass


# class D(C):
#     pass


class MiClase(metaclass=MiMetaClase):
    def __init__(self, a, b):
        print("Objeto de MiClase con a={} y b={}".format(a, b))


# print('creare un objeto ahora...')
# ob1 = MiClase(1, 2)

'''
print('Creando una instancia de la clase...')
m1 = MiClase()
print(m1.atributo_obligatorio)
print(isinstance(MiClase, MiMetaClase))
print(isinstance(MiMetaClase, type))
print(isinstance(int, type))
'''

# a = SoloUna()
# print(a.instance is None)
# b = SoloUna()
# print(a == b)

p1, p2 = Prueba2(nombre='Juan', edad=19)
print(p1)
print(p2)
