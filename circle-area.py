#!/usr/bin/env python3
from math import *
import sys

radius = float(sys.argv[1])

print("The area of a circle with radius {r} is {area}" \
	.format(r=radius, area=pi*radius**2))
