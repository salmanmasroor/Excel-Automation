import pandas as pd
import os

folder_path = "ExcelFiles" 
 

excel_files = []

for file in os.listdir(folder_path):
    if file.endswith(".xlsx") or file.endswith(".xls") or file.endswith(".csv"):
        excel_files.append(file)

# List to store individual DataFrames
dfs = []

for file in excel_files:
    
    file_path = os.path.join(folder_path,file)
    
    df = pd.read_excel(file_path) #read excel files
    
    df['Source_File'] = file  # add column
    dfs.append(df)


master_df = pd.concat(dfs, ignore_index=True)


filename = input("Enter the file Name for storing all data: ")
folder_path = "ExcelFiles/Monthly"
            

output_file = os.path.join(folder_path, f"{filename}.xlsx") 
master_df.to_excel(output_file, index=False)             
        
        



print(f"All files merged successfully into {output_file}")




