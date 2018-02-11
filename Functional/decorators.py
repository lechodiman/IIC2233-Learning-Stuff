# Decorators
import time
from functools import wraps


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'wrapper executed this before {}'.format(original_function.__name__))
            result = original_function(*args, **kwargs)
            print(prefix, 'Excecuted after', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)


# @decorator_function
# def display():
#     print('display function ran')


@prefix_decorator('TESTING: ')
def display_info(name, age):
    print('display_info ran with arguments: ({}, {})'.format(name, age))


display_info('Dave', 26)


# def display():
#     print("display function ran")


# display = decorator_function(display)
# display()

'''
def honorific(original_class):
    class HonorificName(original_class):
        def full_name(self):
            return "Dr. " + ' '.join([self.first_name, self.last_name])

    return HonorificName
'''


def honorific(original_class):
    def new_full_name(self, *args, **kwargs):
        return "Dr. " + ' '.join([self.first_name, self.last_name])

    setattr(original_class, 'full_name', new_full_name)

    return original_class


@honorific
class Name():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return ' '.join([self.first_name, self.last_name])


result = Name('Emmett', 'Brown').full_name()
print('Full name: {0}'.format(result))
