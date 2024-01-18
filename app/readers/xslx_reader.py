import os
import pandas as pd

XLSX_FILENAME = 'tabela-taco_20240117.xlsx'

def read():    
    values = [] 
    data_frame = pd.read_excel(__get_file(), usecols='B, N, D:G, I')
    for _, line in data_frame.iterrows():
        values.append(line.tolist())
    return values    
    

def __get_file():
    current_dir = os.path.dirname(__file__)
    xlsx_path = os.path.join(current_dir, f'../resources/{XLSX_FILENAME}')
    return xlsx_path