import time


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            print(prefix, 'Executed this before :{}'.format(original_function.__name__))
            result = original_function(*args, **kwargs)
            print(prefix, 'Excecuted after: {}'.format(original_function.__name__))
            return result
        return wrapper
    return decorator_function


def my_timer(original_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        finished = time.time() - start
        print('{} Ran in {} secs'.format(original_function.__name__, finished))
        return result
    return wrapper


def honorific(original_class):
    def new_full_name(self, *args, **kwargs):
        return 'Dr ' + ' '.join([self.first, self.last])

    setattr(original_class, 'full_name', new_full_name)

    return original_class


def honorific(original_class):
    class HonorificName(original_class):
        def full_name(self):
            return 'Dr ' + ' '.join([self.first, self.last])
    return HonorificName


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# Functions or class to be decorated
@honorific
class Name():

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return ' '.join([self.first, self.last])


# alternative way
Name = honorific(Name)


@DecoratorClass
def display_info(name, age):
    print('Display Info ran with arguments: ({}, {})'.format(name, age))


# Equivalent way to write it
display_info = DecoratorClass(display_info)


@my_timer
def get_something():
    return [i for i in range(100000)]


if __name__ == '__main__':
    name = Name('Emmet', 'Brown')
    print(name.full_name())
    print(type(name).__name__)
    # a = get_something()
    # display_info('Dave', 26)
