# 3 Key observation form the acquired dataset:  
# The stock was in an extremely tight trading range — only a ₹16.6 spread across the full dataset, suggesting very low volatility.
# OHLC columns are highly inter-correlated (r ≥ 0.96), while Volume shows weak negative correlation with price.
# Daily returns are nearly flat on average (+0.001%), with the biggest single-day move being just ±0.4%.


import pandas as pd

df = pd.read_csv('./dataset/RELIANCE.csv')

def eda_report(df):
    print("\t\t\tEDA Report")
    print("The shape of the dataset:",df.shape)
    print("The percentage of missing values in each column:")
    print(df.isnull().mean()*100)
    df['Daily Return'] = df['Close'].pct_change() * 100
    df['Price Range']  = df['High'] - df['Low']

    print("\nDaily Return stats:\n", df['Daily Return'].describe())
    print("\nPrice Range stats:\n",  df['Price Range'].describe())
    print("\nZero volume days:", (df['Volume'] == 0).sum())
    print("\nCorrelation matrix:\n",df[['Open','High','Low','Close','Volume']].corr().round(3))

if __name__ == "__main__":
    eda_report(df)