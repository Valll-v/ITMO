from math import sqrt
from scipy.optimize import minimize


X1_VALUE = None
X2_VALUE = None


def dist(m1, m2):
    return sqrt((m1[0] - m2[0]) ** 2 + (m1[1] - m2[1]) ** 2)


def func(x):
    if X1_VALUE is not None:
        x1 = X1_VALUE
        x2 = x
    else:
        x1 = x
        x2 = X2_VALUE
    return 7 * x1 ** 2 + 3 * x2 ** 2 + 0.5 * x1 * x2 - 3 * x1 - 5 * x2 + 2


M0 = (2, -2)
print('M0:', M0)
X2_VALUE = M0[1]
Mi = (float(minimize(func, x0=0).x[0]), -2)
print('Mi:', Mi)
d = dist(M0, Mi)
print('Расстояние:', d)


while d >= 0.000001:
    print('_____________________________________')
    M0 = Mi
    if X1_VALUE is not None:
        X1_VALUE = None
        X2_VALUE = M0[1]
        Mi = (float(minimize(func, x0=0).x[0]), M0[1])
        print('Mi:', Mi)
    else:
        X1_VALUE = M0[0]
        X2_VALUE = None
        Mi = (M0[0], float(minimize(func, x0=0).x[0]))
        print('Mi:', Mi)
    d = dist(M0, Mi)
    print('Расстояние:', d)

X1_VALUE = Mi[0]

print(f'result: Mi = {Mi}, f(Mi) = {func(Mi[1])}')
