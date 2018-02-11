# Crea aquí tus decoradores


def comparar_por(atribute):
    def decorator_function(original_class):
        def lower(a, b):
            return getattr(a, atribute) < getattr(b, atribute)

        def greater(a, b):
            return getattr(a, atribute) > getattr(b, atribute)

        def lower_equal(a, b):
            return getattr(a, atribute) <= getattr(b, atribute)

        def greater_equal(a, b):
            return getattr(a, atribute) >= getattr(b, atribute)

        def equal(a, b):
            return getattr(a, atribute) == getattr(b, atribute)

        setattr(original_class, '__lt__', lower)
        setattr(original_class, '__gt__', greater)
        setattr(original_class, '__le__', lower_equal)
        setattr(original_class, '__ge__', greater_equal)
        setattr(original_class, '__eq__', equal)

        return original_class

    return decorator_function


def guardar_instancias(original_class):
    prev_init = getattr(original_class, '__init__')

    def new_init(self, *args, **kwargs):
        prev_init(self, *args, **kwargs)
        original_class.instancias.append(self)

    setattr(original_class, 'instancias', list())
    setattr(original_class, '__init__', new_init)

    return original_class


def cambiar_precio(original_function):
    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        new_result = (result - 100) * (1.23 / 1.19) + 100

        return new_result

    return wrapper


# Debes descomentar las tres líneas comentadas para probar tus decoradores


@guardar_instancias
@comparar_por('altura')
class Hamburguesa:

    def __init__(self, altura, diametro, cantidad_carnes):
        self.altura = altura
        self.diametro = diametro
        self.cantidad_carnes = cantidad_carnes

    def __repr__(self):
        return ('Hamburguesa de {0} cm de altura, '
                '{1} cm de diametro y '
                '{2} carnes').format(self.altura, self.diametro,
                                     self.cantidad_carnes)


@cambiar_precio
def precio_bruto_a_neto(precio_bruto):
    return (precio_bruto * 1.19 + 100)


if __name__ == "__main__":
    hamburguesa1 = Hamburguesa(10, 15, 2)
    hamburguesa2 = Hamburguesa(7, 10, 1)
    hamburguesa3 = Hamburguesa(10, 10, 2)

    print(hamburguesa2 > hamburguesa1)
    print(hamburguesa2 == hamburguesa3)
    print(hamburguesa1 < hamburguesa3)

    print(Hamburguesa.instancias)
    hamburguesa4 = Hamburguesa(12, 20, 4)
    print(Hamburguesa.instancias)

    print(precio_bruto_a_neto(2000))
