class Reverse():

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Optional way to do it, as it is a generator,
# the next function will behave as expected
class Reverse2():

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        while self.index > 0:
            self.index -= 1
            yield self.data[self.index]


if __name__ == '__main__':
    rev = Reverse2('Nice')
    for char in rev:
        print(char)
