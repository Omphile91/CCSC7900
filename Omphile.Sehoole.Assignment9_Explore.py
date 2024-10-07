# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:32:45 2024

@author: S1004826
"""

import os
import netCDF4 as nc
import xarray as xr

# Define the directory and file name explicitly
directory = r'C:\Users\Public\Documents'
file_name =  'Precipitation-Flux_C3S-glob-agric_AgERA5_20240101_final-v1.1.area-subset.-20.15.-35.35.nc'
file_path = os.path.join(directory, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        print("----------------------------------------------------------------")
        # Option 1: using netCDF4
        # Open the netCDF file
        with nc.Dataset(file_path, 'r') as datasetA:
             # Print dataset information
             print(f"Dataset information:\n{datasetA}")
             print("----------------------------------------------------------------")
             # Print dimensions only
             print("Dimensions:")
             for name, dim in datasetA.dimensions.items():
                 print(f"{name}: {dim.size}")
             print("----------------------------------------------------------------")
             # Print variables, type & dimensions
             print("Variables:")
             for name, var in datasetA.variables.items():
                 print(f"{name}: {var.datatype}, dimensions: {var.dimensions}, shape: {var.shape}")
                 # Print min and max values for numeric variables
                 # With netCDF4 you need to explicitly load the data using array slicing
                 # Loading large datasets can be inefficient and might cause memory issues
                 
        print("\n===============================================================")
    
        # Option 2: using xarray
        # Open the netCDF file
        datasetB = xr.open_dataset(file_path)
        # Print dataset information
        print(f"\nDataset information:\n{datasetB}")
        print("----------------------------------------------------------------")
        # Print dimensions only
        print("Dimensions:")
        for name, size in datasetB.dims.items():
            print(f"{name}: {size}")
        print("----------------------------------------------------------------")
        # Print variables, type & dimensions
        print("Variables:")
        for name, var in datasetB.variables.items():
            print(f"{name}: {var.dtype}, dimensions: {var.dims}, shape: {var.shape}")
            # Print min and max values for numeric variables
            if var.dtype.kind in 'fi':  # Check if the variable is float or integer
                print(f"  - Min: {var.min().values}, Max: {var.max().values}")
        print("----------------------------------------------------------------")
        # Print coordinates only
        print("Coordinates:", datasetB.coords)
        print("----------------------------------------------------------------")
        # Print attributes only
        print("Attributes:", datasetB.attrs)
        print("----------------------------------------------------------------")
        # Note: xarray uses lazy loading. To load the data into memory, call .load() on the dataset or specific variables

    except OSError as e:
        print(f"Error opening file: {e}")
