class A:

    def __init__(self):
        print('A constructor ran')
        self.atr = 'A atr'

    def a_method(self):
        return 'A'


class B:

    def __init__(self):
        print('B constructor ran')
        self.atr = 'B atr'

    def a_method(self):
        return 'B'


class C(A, B):

    def __init__(self):
        super().__init__()

        # def a_method(self):
        #     return 'C'

if __name__ == '__main__':
    c = C()
    print(c.atr)
    print(c.a_method())
