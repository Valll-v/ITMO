from math import log


def func(x):
    return 1/3 * x ** 3 - 5 * x + x * log(x)


def dfunc(x):
    return x ** 2 - 4 + log(x)


def ddfunc(x):
    return 2 * x + 1 / x


def get__x(x0):
    return x0 - dfunc(x0) / ddfunc(x0)


def main():
    a = 1.5
    b = 2
    e = 0.02
    x_i = get__x(x0=(a + b) / 2)
    print(f'x0: {(a + b) / 2}')
    print(f'x1: {x_i}')
    d_x_i = dfunc(x_i)
    print(f'f\'(x1): {d_x_i}')
    while abs(d_x_i) >= e:
        print('_______________________')
        x_i = get__x(x0=x_i)
        d_x_i = dfunc(x_i)
        print(f'xi: {x_i}')
        print(f'f\'(xi): {d_x_i}')
    print('result')
    print(f'x = {x_i}; y = {func(x_i)}')


main()
