# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:15:54 2024

@author: S1004826
"""
import numpy as np

import matplotlib.pyplot as plt

 

# Step 1: Load the dataset from the text file

file_path =r'C:\Users\Public\Documents\SOI data.txt'

def processed_data(file_path):

    index_values = []

    with open(file_path, 'r') as file:

        for line in file:

            # Convert each line to a list of floats, handling errors

            try:

                values = list(map(float, line.split()))

                if len(values) > 1 and -999.9 not in values:

                    index_values.append(values)

            except ValueError:

                # Skip lines that can't be converted to floats

                continue

    return np.array(index_values)


index_values_np = processed_data(file_path)

 
if index_values_np.size == 0:

    raise ValueError("Invalid Data Point.")

 

# Extract the years and SOI values

years = index_values_np[:, 0]  # First column (years)

soi_data = index_values_np[:, 1:]  # Remaining columns (SOI index values for each month)

 

# Step 2: Calculate the average index value for each month across all years

monthly_avg = np.mean(soi_data, axis=0)

print("Monthly Averages:\n", monthly_avg)

 

# Step 3: Calculate the standard deviation for each month across all years

monthly_std = np.std(soi_data, axis=0)

print("Monthly Standard Deviations:\n", monthly_std)

 

# Step 4: Identify the years with the maximum and minimum index values for each month

max_indices = np.argmax(soi_data, axis=0)

min_indices = np.argmin(soi_data, axis=0)

 

max_years = years[max_indices]

min_years = years[min_indices]

 

print("Years with Maximum Index Values:\n", max_years)

print("Years with Minimum Index Values:\n", min_years)

 

# Step 5: Calculate the average index value for each year

annual_avg = np.mean(soi_data, axis=1)

print("Annual Average Index Values:\n", annual_avg)

 

# Step 6: Plot the time series of the monthly index values

plt.figure(figsize=(12, 6))

for i in range(soi_data.shape[1]):

    plt.plot(years, soi_data[:, i], label=f'Month {i+1}')

plt.xlabel('Year')

plt.ylabel('SOI Index')

plt.title('Time Series of Monthly SOI Index Values')

plt.legend(loc='upper right')

plt.grid(True)

plt.show()

 

# Step 7: Plot the monthly mean index values with standard deviation

plt.figure(figsize=(10, 5))

months = np.arange(1, soi_data.shape[1] + 1)

plt.bar(months, monthly_avg, yerr=monthly_std, alpha=0.7, capsize=5)

plt.title('Monthly Mean SOI Index Values with Standard Deviation')

plt.xlabel('Month')

plt.ylabel('Mean SOI Index')

plt.xticks(months, [f'Month {i}' for i in months])

plt.grid(True)

plt.show()

 

# Step 8: Plot the annual mean index values

plt.figure(figsize=(12, 6))

plt.plot(years, annual_avg, marker='o', color='b')

plt.title('Annual Mean SOI Index Values')

plt.xlabel('Year')

plt.ylabel('Annual Average SOI Index')

plt.grid(True)

plt.show()


