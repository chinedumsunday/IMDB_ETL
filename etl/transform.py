import pandas as pd 
import numpy as np 

#TRANSFORM
def transform(dataframe):
    for column in list(dataframe.column):
        column.fillna("Unknown", inplace=True)

        