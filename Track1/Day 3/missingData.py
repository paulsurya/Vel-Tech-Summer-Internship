import pandas as pd
df = pd.read_csv('./datasets/titanic.csv',delimiter=',')

#print the percentage of missing data for each column
print("Missing data percentage for each column:")
print(df.isnull().mean()[df.isnull().any()] * 100)

#fill missing values with appropriate values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna('Unknown')
df['Embarked'] = df['Embarked'].fillna('Unknown')

#printing the final dataframe after filling missing values
print("\nDataframe after filling missing values:")
print(df[['Age', 'Cabin', 'Embarked']].head())