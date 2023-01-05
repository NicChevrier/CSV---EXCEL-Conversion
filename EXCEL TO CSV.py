import pandas as pd

# Read in the Excel file
df = pd.read_excel('file.xlsx')

# Convert the Excel file to a CSV file
df.to_csv('file.csv', index=False)
