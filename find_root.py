#!/usr/bin/env python3
def f(x):
    return x**5 + x + 1

def midpoint(a, b):
    return (a + b) / 2

def find_root(f, a, b, epsilon=1e-6, max_iter=100):
    i = 0
    c = midpoint(a, b)

    while abs(f(c)) > epsilon and i < max_iter:
        c = midpoint(a, b)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1

    return c

print(find_root(lambda x: x**5 + x + 1, -1.0, 1.0))
