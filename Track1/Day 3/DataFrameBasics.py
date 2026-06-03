import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Aarav', 'Priya', 'Rohit', 'Sneha', 'Karthik', 'Divya', 'Arjun', 'Meera'],
    'Age': [20, 21, 19, 22, 20, 21, 19, 22],
    'City': ['Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Pune', 'Kolkata', 'Jaipur'],
    'Marks': [85, 45, 90, 32, 78, 55, 92, 40]
})


print(df.head())
print(df.shape)
print(df.dtypes)
df['result'] = np.where(df.Marks >= 50, 'Pass', 'Fail')
print(df)