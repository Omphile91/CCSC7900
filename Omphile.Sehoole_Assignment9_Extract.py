# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:22:24 2024

@author: S1004826
"""

import os
import xarray as xr

# Define the directory and file name explicitly
directory =r'C:\Users\Public\Documents'
file_name = 'Precipitation-Flux_C3S-glob-agric_AgERA5_20240101_final-v1.1.area-subset.-20.15.-35.35.nc'
file_path = os.path.join(directory, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        print("----------------------------------------------------------------")
        # Open the netCDF file
        dataset = xr.open_dataset(file_path)
        
        # Example 1: Extract the entire temperature dataset
        pflux_data = dataset['Precipitation_Flux']  # Use the variable name from the dataset
        # Print basic information about the data
        print(f"Precipitation Data Shape: {pflux_data.shape}")
        print(f"Precipitation Data:\n{pflux_data}")
        print("----------------------------------------------------------------")
        # Example 2: Extract temperature data for a specific time step (only 1 available in this case)
        pflux_at_time = pflux_data.sel(time='2024-01-01')
        # Print shape and data
        print(f"Precipitation at 2024-01-01:\n{pflux_at_time}")
        print("----------------------------------------------------------------")
        # Example 3: Extract temperature data for a specific location (e.g. lat = -29.11, lon = 26.19)
        pflux_at_location = pflux_data.sel(lat=-29.11, lon=26.19, method='nearest')
        actual_lat = pflux_at_location['lat'].values
        actual_lon = pflux_at_location['lon'].values
        # Print the temperature at specified location
        print(f"Precipitation at lat={actual_lat}, lon={actual_lon}:\n{pflux_at_location.values}")
        print("----------------------------------------------------------------")
        # Example 4: Extract temperature data for a specific region (e.g. Lesotho)
        pflux_region = pflux_data.sel(lat=slice(-28.57, -30.68), lon=slice(27.01, 29.45))
        # Print the extracted regional data
        print(f"Precipitation data for the region lat=-28.57 to -30.68 and lon=27.01 to 29.45:\n{pflux_region}")
    
    except OSError as e:
        print(f"Error opening file: {e}")
