import pandas as pd

# Read in the CSV file
df = pd.read_csv('file.csv')

# Convert the CSV file to an Excel spreadsheet
df.to_excel('file.xlsx', index=False)
