class Abstract(type):

    def __new__(meta, name, bases, dic):
        abstract_methods = {k for k, v in dic.items() if getattr(v, 'is_abstract', False)}
        is_abstract = True
        for base in bases:
            if type(base) == meta:
                is_abstract = False
        dic['is_abstract'] = is_abstract
        if is_abstract:
            dic['abstract_methods'] = abstract_methods

        return super().__new__(meta, name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if cls.is_abstract:
            raise Exception('No se puede instancia clase abstracta')

        for name in cls.abstract_methods:
            method = getattr(cls, name)
            if getattr(method, 'is_abstract', False):
                raise Exception('Se debe implementar el metodo', name)
        return super().__call__(*args, **kwargs)


def abstract(original_function):
    original_function.is_abstract = True
    return original_function


class Zorro(metaclass=Abstract):

    def __init__(self, color_pelaje):
        self.color_pelaje = color_pelaje
        print('\nInstancia de Zorro ya creada')

    @abstract
    def cazar(self):
        pass

# Zorro = Abstract('Zorro', (), dict())


class ZorroDarwin(Zorro):
    def cazar(self):
        pass

# ZorroDarwin = Abstract('ZorroDarwin', (Zorro, ), dict())

zorrito = ZorroDarwin('cafe')
