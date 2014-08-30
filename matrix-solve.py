#!/usr/bin/env python3
import scipy.linalg as linalg

a = [[1, 1, 1], [0, 2, 5], [2, 5, -1]]
b = [6, -4, 27]
x = linalg.solve(a, b)

print(x)
