def square_numbers(nums):
    for i in nums:
        yield(i * i)


def double_inputs():
    while True:
        x = yield
        yield x * 2


def generator_function():
    while True:
        val = yield
        print(val)

if __name__ == '__main__':
    g = generator_function()
    next(g)
    g.send('Holi')
    g.send('Chao')
    # gen = double_inputs()
    # next(gen)
    # print(gen.send(10))
    # print(gen.send(20))
