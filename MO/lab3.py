from math import log


def func(x):
    return 1/3 * x ** 3 - 5 * x + x * log(x)


def main(x1, step, e1, e2, x2=None, x3=0, f1=0, f2=0, f3=0):
    if x2 is None:
        x2 = x1 + step
        f1 = func(x1)
        f2 = func(x2)
        if f1 > f2:
            x3 = x1 + 2 * step
        else:
            x3 = x1 - step
        f3 = func(x3)

    print(f'''
x1: {x1} x2: {x2} x3: {x3};
f1: {f1} f2: {f2} f3: {f3};
    ''')

    if f1 <= f2 and f1 <= f3:
        f_min = f1
        x_min = x1
    elif f2 <= f1 and f2 <= f3:
        f_min = f2
        x_min = x2
    else:
        f_min = f3
        x_min = x3

    _x = 1 / 2 * ((x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 + (x1 ** 2 - x2 ** 2) * f3)
    _x_z = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
    print(f'_x_z: {_x_z}')
    if round(abs(_x_z), 6) == 0:
        return main(x_min, step, e1, e2)

    _x /= _x_z
    print(f'_x: {_x}')

    f_x = func(_x)
    cond_r_1 = abs((f_min - f_x) / f_x)
    cond_r_2 = abs((x_min - _x) / f_x)
    cond1 = cond_r_1 < e1
    cond2 = cond_r_2 < e2
    print(cond_r_1, cond_r_2)
    print(cond1, cond2)

    if cond2 and cond1:
        return print(f'result: x = {_x}\n        y = {func(_x)}\n')

    if min(x1, x2, x3) <= _x <= max(x1, x2, x3):
        sorted_x = sorted([x1, x2, x3, _x])
        for i in range(3):
            if min(x_min, _x) == sorted_x[i]:
                x1, x2, x3 = sorted_x[i - 1], min(x_min, _x), sorted_x[i + 1]
                f1, f2, f3 = func(x1), func(x2), func(x3)
                return main(x1, step, e1, e2, x2, x3, f1, f2, f3)
    return main(_x, step, e1, e2)


main(x1=1.5, step=0.5, e1=0.0001, e2=0.0001)
