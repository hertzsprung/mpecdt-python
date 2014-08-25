#!/usr/bin/env python3
import sys
from math import *

a = float(sys.argv[1])
b = float(sys.argv[2])

mean = (a + b) / 2.0
print("{:.2g}".format(ceil(mean)))
