import pandas as pd
import pprint

def eda_report(df):
    report = {}
    
    # Basic Information
    report['shape'] = df.shape
    report['columns'] = df.columns.tolist()
    report['data_types'] = df.dtypes.to_dict()
    
    # Missing Values
    report['missing_values'] = df.isnull().sum().to_dict()
    
    # Descriptive Statistics
    report['descriptive_stats'] = df.describe().to_dict()
    
    return report

# Example usage:
df1 = pd.read_csv('./datasets/titanic.csv',delimiter=',')
df2 = pd.read_csv('./datasets/student-mat.csv',delimiter=';')

report1 = eda_report(df1)
report2 = eda_report(df2)

print("Titanic EDA Report:")
print(pprint.pformat(report1))
print("\nStudent Performance EDA Report:")
print(pprint.pformat(report2))
