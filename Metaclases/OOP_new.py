class Sample:

    def __init__(self, *args):
        print('Sample init ran with args : {}'.format(args))

    def __str__(self):
        return 'SAMPLE'


class A:
    instance = 0

    def __new__(cls, *args):
        print('\nNew was called with args: {}'.format(args))
        print('cls: {}'.format(cls))
        if cls.instance > 0:
            raise Exception('Class is Singleton')
        else:
            instance = super().__new__(cls)
            cls.instance += 1
            instance.new_atr = 'I was created inside new'
            return instance

    def __init__(self, *args):
        self.atr = 'I am an atribute'
        print('\nInit was called with args: {}'.format(args))


if __name__ == '__main__':
    '''
    New is called to CREATE an object, then the object is
    going to be instantiated depending its class
    '''
    a = A('holi')
    print(a)
