# Custon exceptions


class NameTooShort(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShort(name)


class HamsterException(Exception):
    def __init__(self, hamster):
        self.hamster = hamster

    def __str__(self):
        return '{} has escaped!'.format(self.hamster)


class GoatException(Exception):
    message = 'A Goat has eaten your coat'


class AnimalException(Exception):
    def __init__(self, something, animal_type):
        self.something = something
        self.animal_type = animal_type

    def __str__(self):
        msg = 'ERROR: {} \nTIPO DE ERROR: {}'.format(self.something, self.animal_type)

        return msg


class MyError(Exception):
    def __init__(self, error_type, consult):
        self.error_type = error_type
        self.consult = consult

    def __str__(self):
        msg = 'TIPO DE ERROR: {}'.format(self.error_type)
        msg += 'ERROR: {}'.format(self.consult)
        return msg


consults = ['consult_1', 'consult_2', 'consult_3']


def process_consults(consult):
    if consult == 'consult_2':
        raise MyError('Error de tipo', consult)
    elif consult == 'consult_3':
        raise MyError('Error matematico', consult)
    else:
        print('all good')


for i in consults:
    try:
        process_consults(i)
    except MyError as e:
        print(e)
        print('ERROR: {}'.format(i))


'''
something = 'A cat'
try:
    if something is not None:
        raise AnimalException(something, 'HamsterError')

except AnimalException as e:
    output = str(e)
    print(output)
'''
