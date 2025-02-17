def func(x1, x2):
    return 7 * x1 ** 2 + 3 * x2 ** 2 + 0.5 * x1 * x2 - 3 * x1 - 5 * x2 + 2


def f_dx1(x1, x2):
    return 14 * x1 + 0.5 * x2 - 3


def f_dx2(x1, x2):
    return 6 * x2 + 0.5 * x1 - 5


def main():
    x1, x2 = 2, -2
    step = 0.02
    e = 0.0001
    gr_x1 = f_dx1(x1, x2)
    gr_x2 = f_dx2(x1, x2)
    res_prev = func(x1, x2)
    print(f'M0: {x1, x2}')
    print(f'f(M0): {res_prev}')
    print(f'Grad: {gr_x1, gr_x2}')
    x1 = x1 - step * gr_x1
    x2 = x2 - step * gr_x2
    print(f'Mi: {x1, x2}')
    res_new = func(x1, x2)
    print(f'f(Mi): {res_new}')
    while abs(res_new - res_prev) >= e:
        print('_________________________________')
        x1 = x1 - step * gr_x1
        x2 = x2 - step * gr_x2
        print(f'Mi: {x1, x2}')
        res_prev = res_new
        res_new = func(x1, x2)
        print(f'f(Mi): {res_new}')
        while res_new < res_prev:
            x1 = x1 - step * gr_x1
            x2 = x2 - step * gr_x2
            print(f'Mi: {x1, x2}')
            res_prev = res_new
            res_new = func(x1, x2)
            print(f'f(Mi): {res_new}')
        gr_x1 = f_dx1(x1, x2)
        gr_x2 = f_dx2(x1, x2)
        print(f'Grad: {gr_x1, gr_x2}')
    print(x1, x2)



main()
