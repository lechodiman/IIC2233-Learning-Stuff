from abc import ABCMeta, abstractmethod, abstractproperty


class A(metaclass=ABCMeta):
    def __init__(self):
        self.tipo = "holi"
        self.c_base = 0

    @abstractproperty
    def calidad(self):
        if self.check_type() is True:
            return self.c_base + 50
        else:
            return self.c_base

    @abstractmethod
    def check_type(self):
        return True


class B(A):
    def __init__(self):
        self.c_base = 50
        self.tipo = "no holi"

    def check_type(self):
        super().check_type()

    @property
    def calidad(self):
        return self.c_base

if __name__ == '__main__':
    b = B()

    print(b.calidad)
    b.c_base = 0
    print(b.calidad)
