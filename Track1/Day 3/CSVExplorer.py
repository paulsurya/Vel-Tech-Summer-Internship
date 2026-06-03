import pandas as pd

df = pd.read_csv('./datasets/student-mat.csv',delimiter=';')

print(df.shape)
print(df.columns)
print(df.head(3))
print(df.tail(3))
hasInternet = df['internet'].value_counts()['yes']
print(f'Number of students with internet access: {hasInternet}')
print(f'Number of students without internet access: {df.shape[0] - hasInternet}')