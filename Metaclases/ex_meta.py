class MetaExamen(type):
    v1 = []

    def __call__(cls, *args, **kw):
        print('\nCall ran')
        instance = super().__call__(*args, **kw)
        print('Type of instance in call: {}'.format(type(instance)))
        return instance
        # while(len(cls.v1) < args[0]):
        #     cls.v1.append(super().__call__(*args, **kw))
        # return cls.v1


class Pregunta(metaclass=MetaExamen):
    cont = 0

    def __new__(cls, *args, **kwargs):
        print('\nNew ran')
        instance = super().__new__(cls)
        print('Type of instance in new: {}'.format(type(instance)))
        return instance

    def __init__(self, n):
        print('\nInit ran')
        self.id_ = Pregunta.cont
        Pregunta.cont += 1

    def __repr__(self):
        return str(self.id_)


if __name__ == '__main__':
    a = Pregunta(7)
    # print(a)
    # print([type(a[i]) for i in range(len(a))])
