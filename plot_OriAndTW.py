#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:37:13 2023

@author: schsu 
"""
import cartopy     as crt
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
#%%============================================================================
fig = plt.figure()

axl  = fig.add_subplot(1,2,1,title='ne_10m_origional',projection=ccrs.PlateCarree())
axl.set_extent([119.9,122.1,21.8,25.4])
axl.coastlines(resolution='10m')
axl.add_feature(crt.feature.OCEAN,facecolor='blue')
axl.add_feature(crt.feature.LAND ,facecolor='gold')

axr  = fig.add_subplot(1,2,2,title='ne_10m_with_TW',projection=ccrs.PlateCarree())
axr.set_extent([119.9,122.1,21.8,25.4])
ocean = crt.io.shapereader.Reader('ne_10m_ocean.shp').geometries()
axr.add_geometries(ocean,axr.projection,facecolor='blue',edgecolor='none')
land = crt.io.shapereader.Reader('ne_10m_land.shp').geometries()
axr.add_geometries(land,axr.projection,facecolor='gold',edgecolor='none')
coastlines = crt.io.shapereader.Reader('ne_10m_coastline.shp').geometries()
axr.add_geometries(coastlines,axr.projection,facecolor='none',edgecolor='black')

plt.show()
#plt.savefig('OriAndTW_new.png')
