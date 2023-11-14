#importing pandas as pd 
import pandas as pd 
from glob import glob

for filename in glob("*.xls"):
    # Read and store content 
    # of an excel file  
    read_file = pd.read_excel (filename) 
    
    # Write the dataframe object 
    # into csv file 
    read_file.to_csv (f"XLS_{filename}.csv",  
                    index = None, 
                    header=True)