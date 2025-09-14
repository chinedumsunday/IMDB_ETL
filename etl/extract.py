import pandas as pd
import numpy as np 

#EXTRACT
def extract(file_path, name):
    if file_path.endswith(".csv"):
        name = pd.read_csv(file_path)
        return name
    
    elif file_path.endswith(".json"):
        name = pd.read_json(file_path)
        return name
    
    name.head()

#EXPLORE
def explore(dataframe):
    print(dataframe.info())
    print(dataframe.columns)
    print(dataframe.describe())
    print(dataframe.isna().sum())
    print(dataframe.duplicated().sum())
    print(dataframe.nunique())
    print(dataframe.shape)
    return dataframe