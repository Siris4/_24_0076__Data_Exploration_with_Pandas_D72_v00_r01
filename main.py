import pandas as pd

# Change directory if the file is in a different location
import os
os.chdir('C:/Users/Siris/Desktop/GitHub Projects 100 Days NewB/_24_0076__Day72_Data Exploration with Pandas_College Major__240807/NewProject/r00-r09 START/r00_env_START')

# Now read the CSV file
df = pd.read_csv('salaries_by_college_major.csv')
print(df)