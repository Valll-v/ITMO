from math import log


def func(x):
    return 1/3 * x ** 3 - 5 * x + x * log(x)


def dfunc(x):
    return x ** 2 - 4 + log(x)


def get__x(a, b):
    return a - dfunc(a) / (dfunc(a) - dfunc(b)) * (a - b)


def main():
    a = 1.5
    b = 2
    e = 0.02
    _x = get__x(a, b)
    d__x = dfunc(_x)
    print('a:', a)
    print('b:', b)
    print(f'_x: {_x}')
    print(f'f\'(_x): {d__x}')
    while abs(d__x) >= e:
        print('_______________________')
        if d__x > 0:
            b = _x
        else:
            a = _x
        print('a:', a)
        print('b:', b)
        _x = get__x(a, b)
        d__x = dfunc(_x)
        print(f'_x: {_x}')
        print(f'f\'(_x): {d__x}')
    print('result')
    print(f'x = {_x}; y = {func(_x)}')



main()
