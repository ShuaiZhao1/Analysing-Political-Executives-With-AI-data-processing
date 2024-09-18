import numpy as np
import pandas as pd

datafile = './../Data/WDI_CSV_2024_06_28/WDICSV.csv'
data = pd.read_csv(datafile)

pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_colwidth', None)  # Display all column content
pd.set_option('display.width', None)  # Adjust display width automatically

print(data['Indicator Name'].value_counts())