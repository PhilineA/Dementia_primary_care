# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.chdir("/Users/frankadolfsen/Documents/Philine")
import pandas as pd  
import numpy as np

import matplotlib.pyplot as plt


#-------Dementia-------------------------
# Load your data
mydata = pd.read_excel("year_CED_dementia.xlsx")
data_dementia = mydata

# Extract the columns you need
years = data_dementia["year_CED"]
percentages = data_dementia["PERCENT"]

# Create the bar plot
plt.figure(figsize=(12, 6))
plt.bar(range(len(years)), percentages, color='orange')

# Set x-axis ticks and labels
plt.xticks(range(len(years)), years, rotation=45)

# Add labels and title
plt.xlabel('Year of index date')
plt.ylabel("Percentage of persons in the ABOARD-GP dementia cohort")

# Show plot
plt.show()
#-----------MCI----------------------
mydata = pd.read_excel("year_CED_MCI.xlsx")
data_mci = mydata

# Extract the columns you need
years = data_mci["year_CED"]
percentages = data_mci["PERCENT"]

# Create the bar plot
plt.figure(figsize=(12, 6))
plt.bar(range(len(years)), percentages, color='orange')

# Set x-axis ticks and labels
plt.xticks(range(len(years)), years, rotation=45)

# Add labels and title
plt.xlabel('Year of index date')
plt.ylabel("Percentage of persons in the ABOARD-GP MCI cohort")

# Show plot
plt.show()

#---------Dementia + MCI in one figure--------------

# Set the width of the bars
bar_width = 0.35

# Define the positions for the bars
index = np.arange(len(data_dementia))

# Plotting
plt.figure(figsize=(12, 6))

# Plot dementia data
plt.bar(index, data_dementia["PERCENT"], bar_width, color='green', label='Dementia')

# Plot MCI data
plt.bar(index + bar_width, data_mci["PERCENT"], bar_width, color='orange', label='MCI')

# Set x-axis ticks and labels
plt.xticks(index + bar_width / 2, data_dementia["year_CED"], rotation=45)

# Add labels and title
plt.xlabel('Year of index date')
plt.ylabel("Percentage of persons in the ABOARD-GP Cohort")
plt.title('Percentage of Dementia and MCI Over the Years')

# Show legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()