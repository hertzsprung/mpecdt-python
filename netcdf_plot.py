#!/usr/bin/env python3
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, shiftgrid
import matplotlib.pyplot as plt
import numpy as np

def load_era40(filename):
    era40 = Dataset(filename, mode='r')
    longitudes = era40.variables['longitude'][:]
    latitudes = era40.variables['latitude'][:]
    t = era40.variables['p2t'][0][:]
    era40.close()
    return longitudes, latitudes, t

longitudes, latitudes, t = load_era40('ECMWF_ERA-40_subset.nc')

basemap = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, \
    llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')
t, longitudes = shiftgrid(180.0, t, longitudes, start=False)
lon, lat = np.meshgrid(longitudes, latitudes)
xi, yi = basemap(lon, lat)

basemap.pcolor(xi, yi, t)
basemap.drawcoastlines()

plt.show()
