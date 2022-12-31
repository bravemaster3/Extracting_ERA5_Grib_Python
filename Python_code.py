# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 04:13:51 2022

@author: Koffi
"""

####################################xarray
#The following stackoverflow link was useful... Look at the correct answer, and if you have more than 1 variable, you may want to open with cfgrib and merge to get a xr dataset. In my case, I only have one variable so I opened directly with xr
#https://stackoverflow.com/questions/67963199/xarray-from-grib-file-to-dataset
import xarray as xr

#You don't need to import the following if you don't use it (readmy first comment on top to understand in which case you may need it)
# import cfgrib

filepath = r"boundary_layer_height.grib"

grib_blh = xr.open_dataset(filepath, engine="cfgrib") #Make sure you set the path to your dataset, or use complete path for filepath
grib_blh #depending on the structure of your data, you can decide what to do in the next steps. use my example grib dataset to help you...

grib_blh_day = grib_blh.resample(time="d", skipna=True).mean() #this will compute the daily means for instance. change to aggregate it however you want. Example, Y for year

#From array to pandas
grib_blh_df = grib_blh_day.to_dataframe()
