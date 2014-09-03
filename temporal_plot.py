#!/usr/bin/env python3
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter

dates = [date(2014, 8, 1), \
	date(2014, 8, 2), \
	date(2014, 8, 3), \
	date(2014, 8, 4)]
magnitudes = [3, 7, 4, 11]

plt.plot_date(dates, magnitudes, linestyle='-')

xaxis = plt.gca().xaxis
xaxis.set_major_locator(DayLocator())
xaxis.set_major_formatter(DateFormatter('%F'))

plt.show()
