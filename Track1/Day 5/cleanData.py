import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/RELIANCE.csv')

#    Dividends and Stock Splits are all zeros → carry zero information
constant_cols = df.columns[df.std() == 0].tolist()
df.drop(columns=constant_cols, inplace=True)
print("Dropped constant columns:", constant_cols)

# Fix zero volume (row 0 — likely a market holiday / data gap)

df['Volume'] = df['Volume'].replace(0, np.nan)
df['Volume'] = df['Volume'].ffill().bfill()

# ── 3. Engineer Daily Return (introduces 1 NaN at row 0) 
df['Daily Return'] = df['Close'].pct_change() * 100

#    Fill that first NaN with 0.0 (no prior day → assume no change)
df['Daily Return'] = df['Daily Return'].fillna(0.0)

# ── 4. Add more meaningful features for your model 
df['Price Range']   = df['High'] - df['Low']           # intraday volatility
df['MA_7']          = df['Close'].rolling(7).mean()    # 7-day moving average
df['MA_21']         = df['Close'].rolling(21).mean()   # 21-day moving average
df['Vol_7_avg']     = df['Volume'].rolling(7).mean()   # volume trend

#    Rolling windows create NaNs at the start — fill with expanding mean
df['MA_7']      = df['MA_7'].fillna(df['Close'].expanding().mean())
df['MA_21']     = df['MA_21'].fillna(df['Close'].expanding().mean())
df['Vol_7_avg'] = df['Vol_7_avg'].fillna(df['Volume'].expanding().mean())

# Final check 
print("\nRemaining nulls:\n", df.isnull().sum())
print("\nFinal shape:", df.shape)
print("\nSample:\n", df.head())