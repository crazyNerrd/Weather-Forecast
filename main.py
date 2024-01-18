# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the weather dataset (replace 'path_to_dataset' with the actual path)
weather_df = pd.read_csv('seattle-weather.csv')

# Display the first few rows of the dataset
print(weather_df.head())

# Get basic information about the dataset
print(weather_df.info())

# Get summary statistics of numerical columns
print(weather_df.describe())
