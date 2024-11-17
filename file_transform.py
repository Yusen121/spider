import pandas as pd

csv_file_path = 'output.csv'
df = pd.read_csv(csv_file_path)

excel_file_path = 'output.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')