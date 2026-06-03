import pandas as pd
df = pd.read_csv('./datasets/student-mat.csv',delimiter=';')

print("=" * 40)
print("   Average G3 by Study Time")
print("=" * 40)
print(df.groupby('studytime')['G3'].mean().to_string())

print("\n" + "=" * 40)
print("   Average Grades by Sex")
print("=" * 40)
print(df.groupby('sex')[['G1','G2','G3']].mean().to_string())

print("\n" + "=" * 40)
print("   Top 5 Students by G3")
print("=" * 40)
print(df.nlargest(5, 'G3')[['G1','G2','G3']].to_string(index=False))