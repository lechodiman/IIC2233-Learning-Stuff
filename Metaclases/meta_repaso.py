
class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, dic):
        '''Handles the CREATION of an object, while init handles the
        instantiation of it '''
        print('\nNew ran')
        print(meta)
        print(nombre)
        dic.update({'peso': 40})
        return super().__new__(meta, nombre, base_clases, dic)

    def __init__(clase, nombre, base_clases, dic):
        print('\nInit ran')

    def __call__(clase, *args, **kwargs):
        print('\nSe llamo a la creacion de una nueva instancia de clase menor')
        print('Call de : {}'.format(clase))
        print('Call con args: {}'.format(args))
        return super().__call__(*args, **kwargs)

    def some_function(clase):
        return 'Clases creadas con esta meta, tendran esta funcion'


class MiClase(metaclass=MiMetaClase):

    def __init__(self, atr):
        print('\nEstamos en init de clase menor')
        self.atr = atr

    def func(self, params):
        pass

    mi_param = 4

# Alternative way to look at it
# MiClase = MiMetaClase('MiClase', (), dict())

if __name__ == '__main__':
    print('\nVoy a crear una instancia')
    instancia = MiClase(1)
    # print(MiClase.some_function())
