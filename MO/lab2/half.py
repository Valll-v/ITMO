from math import log


def func(x):
    return 1/3 * x ** 3 - 5 * x + x * log(x)


def main():
    a = 1.5
    b = 2
    e = 0.02
    while b - a > 2 * e:
        print('_______________________')
        x1 = (a + b - e) / 2
        print('x1:', x1)
        x2 = (a + b + e) / 2
        print('x2:', x2)
        y1 = func(x1)
        print('y1:', y1)
        y2 = func(x2)
        print('y2:', y2)
        if y1 > y2:
            a = x1
        else:
            b = x2
        print('a:', a)
        print('b:', b)
    print('result')
    x = (a + b) / 2
    print(f'x = {x}; y = {func(x)}')


main()
