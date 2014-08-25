#!/usr/bin/env python3
from math import *
import sys

radius = float(sys.stdin.readline())

print("The area of a circle with radius {r} is {area:.4g}" \
	.format(r=radius, area=pi*radius**2))
