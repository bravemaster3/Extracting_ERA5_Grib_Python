# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 04:13:51 2022

@author: Koffi
"""

#https://www.luisalucchese.com/post/how-to-read-grib2-raster-python/
from osgeo import gdal
import numpy as np
# import rasterio as rio
#import os

# os.chdir('C:/Users/kono0001/.conda/envs/ERA5GribExtraction')

filepath = r"boundary_layer_height.grib"

# Open the file:
raster = gdal.Open(filepath)
type(raster)
number_bands = raster.RasterCount

for i in range(1, 5):

    band = raster.GetRasterBand(i)
    data_array = band.ReadAsArray()

    num_list = []

    for row in data_array:
        for value in row:
            if value != 9999:
                num_list.append(value)
    print("band: " + str(i))
    print("Count: " + str(len(num_list)))
    print("Max: " + str(np.max(num_list)))
    print("Min: " + str(np.min(num_list)))
    print("Mean: " + str(np.mean(num_list)))
    print("Standard Deviation: " + str(np.std(num_list)))
    print
    

    

raster.GetRasterBand(1).GetMetadata()

raster.GetRasterBand(2).GetMetadata()


####################################xarray
#The following stackoverflow link was useful... Look at the correct answer, and if you have more than 1 variable, you may want to open with cfgrib and merge to get a xr dataset. In my case, I only have one variable so I opened directly with xr
#https://stackoverflow.com/questions/67963199/xarray-from-grib-file-to-dataset
import xarray as xr
import cfgrib

filepath = r"boundary_layer_height.grib"

# grib_blh = cfgrib.open_datasets(filepath)
grib_blh2 = xr.open_dataset(filepath, engine="cfgrib")
grib_blh2[0]

grib_blh_day = grib_blh2.resample(time="d", skipna=True).mean()

#From array to pandas
grib_blh_df = grib_blh_day.to_dataframe()
