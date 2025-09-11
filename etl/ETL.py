import pandas as pd
import numpy as np 

#EXTRACT

def extract(file_path):
    if file_path.endsWith(".csv"):
        pd.read_csv(file_path)
        