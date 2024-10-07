# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:47:58 2024

@author: S1004826
"""

import os
import xarray as xr
import numpy as np
from datetime import datetime, timedelta

# Define the directory and file name pattern explicitly
directory =r'C:\Users\Public\Documents'
file_pattern = 'Precipitation-Flux_C3S-glob-agric_AgERA5_{date}_final-v1.1.area-subset.-20.15.-35.35.nc'
outfile_pattern = 'Monthly_Precipitation-Flux-Mean_AgERA5_Stats_{date}.nc'

# Specify the start and end dates for the month (January 2024)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)

# List to store daily data
daily_data_list = []

# Loop through each day in the month
current_date = start_date
while current_date <= end_date:
    # Format the date as YYYYMMDD
    date_str = current_date.strftime("%Y%m%d")
    outdate_str = start_date.strftime("%Y%m")
    
    # Construct the file path for the current day
    file_name = file_pattern.format(date=date_str)
    file_path = os.path.join(directory, file_name)
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Open the netCDF file
            dataset = xr.open_dataset(file_path)
            
            # Extract the precipitation data
            pflux_data = dataset['Precipitation_Flux']  # Use the variable name from the dataset
            
            # Append the precipitation data to the list
            daily_data_list.append(pflux_data)
            
        except OSError as e:
            print(f"Error opening file {file_path}: {e}")
    
    else:
        print(f"File not found: {file_path}")
    
    # Move to the next day
    current_date += timedelta(days=1)

# Concatenate the daily data along the 'time' dimension
if daily_data_list:
    monthly_data = xr.concat(daily_data_list, dim='time')
    print(f"Monthly Data Shape: {monthly_data.shape}")
    
    # Step 4: Convert the data to a NumPy array for further manipulation
    monthly_data_np = monthly_data.values
    print(f"Converted to NumPy array, shape: {monthly_data_np.shape}")
    
    # Create a mask where all values are NaN over the time dimension
    nan_mask = np.all(np.isnan(monthly_data_np), axis=0)

    # Suppress warnings for invalid operations (such as NaN mean/max/min)
    np.seterr(invalid='ignore')

    # Instead of calculating the mean on all data directly, handle NaN slices manually
    valid_slices = np.where(~nan_mask)  # Only work on non-NaN slices

    # Calculate the monthly mean precipitation, ignoring NaNs
    monthly_mean_precipitation = np.empty(monthly_data_np.shape[1:], dtype=np.float32)
    monthly_mean_precipitation.fill(np.nan)  # Initialize with NaN

    # Only calculate mean for valid slices
    for i, j in zip(*valid_slices):
        monthly_mean_precipitation[i, j] = np.nanmean(monthly_data_np[:, i, j])

    # Calculate the monthly maximum precipitation
    monthly_max_precipitation = np.nanmax(np.nan_to_num(monthly_data_np, nan=-np.inf), axis=0)
    monthly_max_precipitation[nan_mask] = np.nan  # Restore NaN grid points
    
    # Calculate the monthly minimum precipitation
    monthly_min_precipitation = np.nanmin(np.nan_to_num(monthly_data_np, nan=np.inf), axis=0)
    monthly_min_precipitation[nan_mask] = np.nan  # Restore NaN grid points
    
    # # Convert temperatures from Kelvin to degrees Celsius
    # monthly_mean_temp_celsius = monthly_mean_temp - 273.15
    # monthly_max_temp_celsius = monthly_max_temp - 273.15
    # monthly_min_temp_celsius = monthly_min_temp - 273.15
    
    print(f"Monthly mean precipitation (mm/day) (shape {monthly_mean_precipitation.shape}):\n{monthly_mean_precipitation}")
    
    # Write the results to a new netCDF file
    # Define output file path
    outfile_name = outfile_pattern.format(date=outdate_str)
    output_file = os.path.join(directory, outfile_name)
       
    # Create a new xarray Dataset with the calculated values
    output_dataset = xr.Dataset(
        {
            "Monthly_Mean_Precipitation": (["lat", "lon"], monthly_mean_precipitation),
            "Monthly_Max_Precipitation": (["lat", "lon"], monthly_max_precipitation),
            "Monthly_Min_Precipitation": (["lat", "lon"], monthly_min_precipitation),},
        coords={
            "lat": monthly_data.coords["lat"],
            "lon": monthly_data.coords["lon"],
        },
        attrs={
            "description": "Monthly mean, max, and min precipitation",
            "units": "mm/day",
            "source": "AgERA5",
        },
    )
    
    # Write to netCDF
    output_dataset.to_netcdf(output_file)
    print(f"Monthly precipitation statistics written to {output_file}")
    
else:
    print("No data found for the entire month.")
