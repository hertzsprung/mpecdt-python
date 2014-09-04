#!/usr/bin/env python3
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, shiftgrid
import matplotlib.pyplot as plt
import numpy as np

era40 = Dataset('ECMWF_ERA-40_subset.nc', mode='r')
time = era40.variables['time'][:]
longitudes = era40.variables['longitude'][:]
latitudes = era40.variables['latitude'][:]
u = era40.variables['p10u'][0][:]

era40.close()

basemap = Basemap(projection='merc', llcrnrlat=-80,urcrnrlat=80,\
                    llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
u, longitudes = shiftgrid(180.0, u, longitudes, start=False)
lon, lat = np.meshgrid(longitudes, latitudes)
xi, yi = basemap(lon, lat)

basemap.pcolor(xi, yi, u)
basemap.drawcoastlines()

plt.show()
