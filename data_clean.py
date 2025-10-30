import pandas as pd
import os

input_folder = "ExcelFiles"
output_folder = "ExcelFiles/Cleaned"

os.makedirs(output_folder, exist_ok=True) 

excel_files = [f for f in os.listdir(input_folder) if f.endswith((".xlsx", ".xls"))]

for file in excel_files:
    file_path = os.path.join(input_folder, file)
    df = pd.read_excel(file_path)
    
    
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
  
    text_cols = df.select_dtypes(include='object').columns
    df[text_cols] = df[text_cols].fillna("Unknown")
    
    
    output_path = os.path.join(output_folder, file)
    df.to_excel(output_path, index=False)
    print(f"✅ Cleaned file saved: {output_path}")



