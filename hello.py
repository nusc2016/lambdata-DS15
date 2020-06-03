# Import enlarge function
from pandas import DataFrame
from my_mod import split, date_split


df = DataFrame({'state':['CT','CO','CA','TX']})
print(df.head())

# Invoke split
split(df)