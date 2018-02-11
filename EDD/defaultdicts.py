from collections import defaultdict


class Integer:

    def __init__(self, num=0):
        self.num = num

    def __call__(self):
        return self.num

    def __str__(self):
        return str(self.num)


dos = Integer(2)

# argument must be callable, eg, int, str, dos, etc
d = defaultdict(list)

if __name__ == '__main__':
    print(d['holi'])
