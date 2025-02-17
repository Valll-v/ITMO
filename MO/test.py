from scipy.optimize import minimize


def func(x):
    return 3 * x ** 2 + 0.14285 * x


print(minimize(func, x0=0))