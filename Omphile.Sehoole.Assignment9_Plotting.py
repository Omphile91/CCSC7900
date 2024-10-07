# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:08:43 2024

@author: S1004826
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
from datetime import datetime
import numpy as np
import matplotlib.ticker as ticker

# Define the directory and filename pattern
directory = r'C:\Users\Public\Documents'
outfile_pattern = 'Monthly_Precipitation-Flux-Mean_AgERA5_Stats_{date}.nc'
# Capture the current date (or use the date for the processed data)
start_date = datetime(2024, 1, 1)  # You can adjust the start date
outdate_str = start_date.strftime("%Y%m")  # Format the date as YYYYMM for output filename
# Construct the output file name dynamically
outfile_name = outfile_pattern.format(date=outdate_str)
output_file = os.path.join(directory, outfile_name)

# Load the netCDF file
dataset = xr.open_dataset(output_file)

# Extract temperature variables (in degrees Celsius)
mean_precipitation = dataset["Monthly_Mean_Precipitation"]
max_precipitation = dataset["Monthly_Max_Precipitation"]
min_precipitation= dataset["Monthly_Min_Precipitation"]

# Extract coordinates
lat = dataset["lat"]
lon = dataset["lon"]

# Set consistent precipitation scale (0 to 5 mm/day)
vmin, vmax = 0, 10  # Min and max precipitation for the colour scale
levels = np.linspace(vmin, vmax, 10)  # 10 contour levels between 0 and 5 mm/day

# Create plots using matplotlib with Cartopy
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot Monthly Mean Precipitation
contour = axes[0].contourf(lon, lat, mean_precipitation, cmap="coolwarm", levels=levels, vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())
axes[0].add_feature(cfeature.COASTLINE)
axes[0].add_feature(cfeature.RIVERS)
axes[0].set_title('Monthly Mean Precipitation (mm/day)')
cbar = plt.colorbar(contour, ax=axes[0], label='Precipitation (mm/day)', shrink=0.7, aspect=15, pad=0.02)
cbar.ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Remove decimal places

# Plot Monthly Maximum Precipitation
contour = axes[1].contourf(lon, lat, max_precipitation, cmap="coolwarm", levels=levels, vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())
axes[1].add_feature(cfeature.COASTLINE)
axes[1].add_feature(cfeature.RIVERS)
axes[1].set_title('Monthly Max Precipitation (mm/day)')
cbar = plt.colorbar(contour, ax=axes[1], label='Precipitation (mm/day)', shrink=0.7, aspect=15, pad=0.02)
cbar.ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Remove decimal places

# Plot Monthly Minimum Precipitation
contour = axes[2].contourf(lon, lat, min_precipitation, cmap="coolwarm", levels=levels, vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())
axes[2].add_feature(cfeature.COASTLINE)
axes[2].add_feature(cfeature.RIVERS)
axes[2].set_title('Monthly Min Precipitation (mm/day)')
cbar = plt.colorbar(contour, ax=axes[2], label='Precipitation (mm/day)', shrink=0.7, aspect=15, pad=0.02)
cbar.ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Remove decimal places

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
