#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:29:31 2024

@author: PhilineAdolfsen
"""

import os
import pandas as pd
import numpy as np
from random import choices
import matplotlib.pyplot as plt

#choose directory
os.chdir('/Users/PhilineAdolfsen/Desktop/PHARMO/python_scripts')


#---------------Dementia-----------------
#loading data
df = pd.read_excel('patients_overtime_dementia.xlsx')

# Remove the "size" prefix from column names and placing the rows in the right order
df.columns = df.columns.str.replace('size', '')
df.iloc[[1, 2]] = df.iloc[[2, 1]]
df.iloc[[3, 4]] = df.iloc[[4, 3]]

# Extract relevant rows and columns
df_plot = df.iloc[1:][['type'] + [col for col in df.columns if col.isdigit()]]

# Set 'type' as the index for easy plotting
df_plot.set_index('type', inplace=True)

# Transpose the DataFrame for easy plotting
df_plot = df_plot.T

# Define a custom color palette
colors = ['orange','red', 'green', 'yellow']

# Plot the stacked bar plot with the custom color palette
ax = df_plot.plot(kind='bar', stacked=True, figsize=(12, 6), color=colors)

# Customize the x-tick labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Adjust rotation if necessary

# Customize the plot
ax.set_xlabel('Year')
ax.set_ylabel('Number of Patients')
ax.set_title('Dementia patients over the years')


# Show the plot
plt.show()


#----------MCI-----------------
#loading data
df = pd.read_excel('patients_overtime_mci.xlsx')

# Remove the "size" prefix from column names and placing the rows in the right order
df.columns = df.columns.str.replace('size', '')
df.iloc[[1, 4]] = df.iloc[[4, 1]]
df.iloc[[1, 2]] = df.iloc[[2, 1]]
df.iloc[[3, 4]] = df.iloc[[4, 3]]

# Extract relevant rows and columns
df_plot = df.iloc[1:][['type'] + [col for col in df.columns if col.isdigit()]]

# Set 'type' as the index for easy plotting
df_plot.set_index('type', inplace=True)

# Transpose the DataFrame for easy plotting
df_plot = df_plot.T

# Define a custom color palette
colors = ['orange','red', 'green', 'yellow']

# Plot the stacked bar plot with the custom color palette
ax = df_plot.plot(kind='bar', stacked=True, figsize=(12, 6), color=colors)

# Customize the x-tick labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Adjust rotation if necessary

# Customize the plot
ax.set_xlabel('Year')
ax.set_ylabel('Number of Patients')
ax.set_title('MCI patients over the years')

# Show the plot
plt.show()