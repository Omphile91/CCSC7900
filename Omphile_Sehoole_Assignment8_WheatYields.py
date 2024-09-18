# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:20:43 2024

@author: S1004826
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

directory = r'C:\Users\Public\Documents\CSV Files'
file_name = 'FAOSTAT_data.csv'
file_path = os.path.join(directory, file_name)

# # Define the directory and file name explicitly as provided earlier
# directory = os.getcwd()  # This will set the current directory where the script is running from
# file_name = 'FAOSTAT_data.csv'
# file_path = os.path.join(directory, file_name)

try:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Extract rows where 'Item' is 'Maize (corn)' and 'Element' is 'Yield'
    wheat_yield_data = df[(df['Item'] == 'Wheat') & (df['Element'] == 'Yield')]

    # Select only the 'Year' and 'Value' columns
    annual_yields = wheat_yield_data[['Year', 'Value']]
    
    # Convert the result to a NumPy array
    wheat_yields = annual_yields.values
    
    # Display first few rows of the extracted Year and Yield data
    # print("\nFirst 5 rows of the 'Year' and 'Yield' data for 'Maize (corn)':")
    # print(annual_yields.head())

    # Separate years and yield values into two separate arrays
    years = wheat_yields[:, 0]  # Slicing the first column for the years
    yields = wheat_yields[:, 1]  # Slicing the second column for the yields
    print("Years:", years)
    print("Yields:", yields)
    
    # Reshape yields array to have a single row in stead of a single column
    yields_reshaped = yields.reshape(1, -1)
    
    # Calculate mean and standard deviation
    mean_yield = np.mean(yields)
    print("Mean Yield:", mean_yield)
    
    # Calculate yield anomalies
    anom_yield = (yields - mean_yield)
    print("Deviations:", anom_yield)
    mean_anom = np.mean(anom_yield)
    print("Mean Deviation:", mean_anom)
    
    # Plot the anomalies using a bar plot or line plot
    plt.figure(figsize=(10, 6))
    plt.bar(years, anom_yield, color='b', edgecolor='black')
    #plt.plot(years, anom_yield, marker='o', linestyle='-', color='b')
    
    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Yield Anomaly (Deviation from Mean)  Unit = 100 g/ha')
    plt.title('Wheat Yield Anomalies Over Time')
    
    # Draw a horizontal line at 0 (representing the mean)
    plt.axhline(0, color='red', linestyle='--')

    # Display the plot
    plt.show()
    
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in the directory '{directory}'.")

except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty or corrupted.")

except pd.errors.ParserError:
    print("Error: There was an error parsing the CSV file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")