import pandas as pd
import numpy as np
import glob, os
import joblib
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from sklearn.model_selection import train_test_split

CSV_FOLDER = r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\stockData"

all_files = glob.glob(os.path.join(CSV_FOLDER, "*.csv"))
df_list = []
for f in all_files:
    tmp = pd.read_csv(f)
    df_list.append(tmp)

df = pd.concat(df_list, ignore_index=True)
df.columns = df.columns.str.strip().str.lower()
df = df.loc[:, ~df.columns.duplicated()]

df['date'] = pd.to_datetime(df['date'], dayfirst=False, errors='coerce')
df = df.sort_values(['symbol', 'date']).reset_index(drop=True)

df['target'] = (df.groupby('symbol')['close'].shift(-1) > df['close']).astype(int)

def add_indicators(group):
    group = group.copy()
    group['rsi'] = RSIIndicator(close=group['close'], window=14).rsi()
    group['sma_5'] = SMAIndicator(close=group['close'], window=5).sma_indicator()
    group['sma_20'] = SMAIndicator(close=group['close'], window=20).sma_indicator()
    group['ma_cross'] = group['sma_5'] - group['sma_20']
    group['volatility'] = group['close'].rolling(14).std()
    group['volume_ratio'] = group['volume'] / group['volume'].rolling(20).mean()
    group['vwap_diff'] = group['close'] - group['vwap']
    group['daily_range'] = group['high'] - group['low']
    group['delivery_pct'] = group['%deliverble'].fillna(0)
    return group

print("Loading indicators...")
df = df.groupby('symbol', group_keys=False).apply(add_indicators)

FEATURES = ['rsi', 'ma_cross', 'volatility', 'volume_ratio',
            'vwap_diff', 'daily_range', 'delivery_pct']

df = df.dropna(subset=FEATURES + ['target'])

X = df[FEATURES]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = joblib.load(r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")

y_pred = model.predict(X_test)

correct = (y_pred == y_test).sum()
total = len(y_test)
hit_rate = correct / total * 100

print(f"Backtest hit rate: {hit_rate:.1f}%")
print(f"Correct calls: {correct} out of {total}")

results = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred,
    'Correct': (y_pred == y_test.values)
})

print(results.tail(20))