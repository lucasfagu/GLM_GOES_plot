#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:29:00 2018

@author: lucas

based in http://edc.occ-data.org/goes16/python/#glm-plots
download files in http://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/generic_AWS_download.cgi?DATASET=noaa-goes16&BUCKET=GLM-L2-LCFA/2018/201/18
or https://storage.cloud.google.com/gcp-public-data-goes-16/GLM-L2-LCFA/2018/204/13/OR_GLM-L2-LCFA_G16_s20182041351000_e20182041351200_c20182041351228.nc?_ga=2.258753922.-900149159.1532088996
"""

# import packages 
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# open file
goes_glm = Dataset('/home/lucas/Downloads/OR_GLM-L2-LCFA_G16_s20182011819400_e20182011820000_c20182011820026.nc', mode='r')


flash_lat = goes_glm.variables['flash_lat'][:]
flash_lon = goes_glm.variables['flash_lon'][:]
#flash_energy = goes_glm.variables['flash_energy'][:]

fig = plt.figure(figsize=(6,6),dpi=200)
m = Basemap(projection='cyl', resolution='h',
            lon_0=-10,
            llcrnrlat=-45, urcrnrlat = -20,
            llcrnrlon=-65, urcrnrlon = -40)

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()
m.drawparallels(np.arange(-45,-20,5.),labels=[1,0,0,0], linewidth=0.0)
m.drawmeridians(np.arange(-65.,-40.,5.),labels=[0,0,0,1], linewidth=0.0)
#m.fillcontinents(color='coral',lake_color='aqua')

flash_x, flash_y = m(flash_lon, flash_lat)
m.plot(flash_x, flash_y, 'o',markersize=0.7,color='red')
plt.title('Raios '+ str(goes_glm.time_coverage_end)+' (UTC)')
plt.savefig('Raios '+ str(goes_glm.time_coverage_end)+'(UTC).png')
plt.show()
plt.close()
