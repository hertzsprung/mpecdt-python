#!/usr/bin/env python3
from math import *
import numpy as np
import scipy.linalg as linalg

print(np.dot(3, 4))
print(np.dot([0.5, 2.0], [-3.0, 2.0]))

def create_coefficient_matrix(size, k):
    """Returns a matrix having dimensions size*size populated with the
    coefficients to solve BTCS"""
    m = np.zeros([size, size])

    populate_first_and_last_row_identities(m)
    populate_btcs_coefficients(m, k)

    return m

def populate_first_and_last_row_identities(m):
    size = len(m)
    m[0,0] = 1.0
    m[size-1, size-1] = 1.0

def populate_btcs_coefficients(m, k):
    # each row has three non-zero coefficients that are shifted
    # one column to the right for each row down
    nonzero_coefficients = [-k, 1 + 2*k, -k]
    size = len(m)

    first_nonzero_column = 0
    for row in range(1, size-1):
        for index, coefficient in enumerate(nonzero_coefficients):
            column = (first_nonzero_column + index) % size
            m[row, column] = coefficient
        first_nonzero_column = (first_nonzero_column + 1) % size

xmin = 0.0
xmax = 1.0
dt = 0.1
nx = 40
dx = (xmax - xmin) / nx
K = 1e-3
d = K * dt / (dx**2)
Kdtbydx2 = K*dt/dx**2

def initial_state(xmin, xmax, nx):
	phi = np.zeros(nx)
	for i in range(nx):
		phi[i] = sin(pi*i/nx)
	return phi

phi = initial_state(xmin, xmax, nx)
print(phi)

coefficient_matrix = create_coefficient_matrix(len(phi), Kdtbydx2)

for i in range(40):
	phi = linalg.solve(coefficient_matrix, phi)
print(phi)
