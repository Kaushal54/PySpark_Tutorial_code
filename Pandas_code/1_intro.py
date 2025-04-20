# https://www.youtube.com/watch?v=2uvysYbKdjM
# axis 1 : row & axis 0 : column
# map is for series & apply is for dataFrame

# examples : https://www.w3resource.com/python-exercises/pandas/index.php


import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8], [10, 11, 12]] , columns=['A', 'B', 'C'])
# df = pd.DataFrame([[1,2,3], [4,5,6], [7,8]] , columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])

# print(df.head(3))    # To fetch first 5 records
# print(df.tail(3))    # To fetch last 5 records
# print(df.columns)    # To fetch columns name
# print(df.index.tolist())    # To fetch total index
# print(df.info())    # to get columns wise dataType
# print(df.describe())      # To fetch math calculation column wise
# print(df.nunique())      # To fetch total unique number of values in each column
# print(df['A'].unique())      # To fetch unique values of selected column
# print(df.shape)      # To fetch shape of df [rows X columns]
# print(df.size)      # returns the total number of elements in the DataFrame. This is calculated as the number of rows multiplied by the number of columns. Output will be 9 (3 rows * 3 columns)
# print(df.sample(3, random_state=42))      # returns any random rows
