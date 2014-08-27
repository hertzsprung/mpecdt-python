#!/usr/bin/env python3
from math import *

def circle_area(radius):
	return pi*radius**2

def print_circle_area(radius, area):
	print("The area of a circle " + \
	"with radius {r} is {area:.4g}" \
	.format(r=radius, area=area))

radius = 4.5
area = circle_area(radius)
print_circle_area(radius, area)
