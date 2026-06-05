import pandas as pd

df = pd.read_csv('./dataset/RELIANCE.csv')

print("-"*20)
print("The shape of the dataset:",df.shape)
print("The columns in the dataset:",df.columns)
print("The first 5 rows of the dataset:")
print(df.head())
print("The datatypes of the columns:")
print(df.dtypes)
print("-"*20)