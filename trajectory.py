#!/usr/bin/env python3
from math import *
from scipy.optimize import fmin_cg
g=9.81
target_distance=25.0
mag=20

def x_distance(u0, t):
    return u0*t

def time_in_air(w0):
    return 2*w0/g

def landing_distance(u0, w0):
    return x_distance(u0, time_in_air(w0))

def componentise(elevation_angle, mag):
    return cos(elevation_angle)*mag, sin(elevation_angle)*mag

def distance_from_target(elevation_angle_array):
    elevation_angle = elevation_angle_array[0]
    print('*** attempting angle pi*' + str(elevation_angle/pi))
    u0, w0 = componentise(elevation_angle, mag)
    return landing_distance(u0, w0) - target_distance

print('------')
print(landing_distance(10, 10))
xopt = fmin_cg(distance_from_target, 0.0) # letting fmin_cg approximate gradients for now
