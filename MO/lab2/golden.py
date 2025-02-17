from math import log


def func(x):
    return 1/3 * x ** 3 - 5 * x + x * log(x)


def main():
    a = 1.5
    b = 2
    e = 0.00002
    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618 * (b - a)
    y1 = func(x1)
    y2 = func(x2)
    while b - a > 2 * e:
        print('x1:', x1)
        print('x2:', x2)
        print('y1:', y1)
        print('y2:', y2)
        if y1 < y2:
            b = x2
            x2 = x1
            x1 = a + 0.382 * (x2 -a)
            y1 = func(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + 0.618 * (b - x1)
            y2 = func(x1)
        print('a:', a)
        print('b:', b)
        print('_______________________')
    print('result')
    x = (a + b) / 2
    print(f'x = {x}; y = {func(x)}')


main()
