import numpy as np
import pandas as pd
import os

path = "C:/Users/Marta Gajewska/OneDrive - McKinsey & Company/Documents/PROJECTS/37_nanodegree/Project 1 - SDG/data"
os.chdir(path)

def read_input_file(file_path):
    df = pd.read_excel(file_path,
        engine='openpyxl',
        usecols=['Goal', 'Target', 'GeoAreaCode', 'GeoAreaName', 'TimePeriod', 'Value'])
    df = df[df['TimePeriod'].between(2008,2012) | df['TimePeriod'].between(2018,2021)]
    return(df)

arr = []  
print(os.listdir())

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".xlsx"):
        file_path = f"{path}\{file}"
        # call read input file function
        arr.append(read_input_file(file_path))
        

print(arr)