import pandas as pd
import numpy as np
import glob, os
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

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

print("Adding indicators... this may take a minute")
df = df.groupby('symbol', group_keys=False).apply(add_indicators)
print("Done!")

FEATURES = ['rsi', 'ma_cross', 'volatility', 'volume_ratio',
            'vwap_diff', 'daily_range', 'delivery_pct']

df = df.dropna(subset=FEATURES + ['target'])

X = df[FEATURES]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

neg = (y_train == 0).sum()
pos = (y_train == 1).sum()
spw = round(neg / pos, 2)

model = XGBClassifier(
    eval_metric='logloss',
    random_state=42,
    scale_pos_weight=spw,
    learning_rate=0.1,
    n_estimators=200,
    max_depth=7
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("F1 Score:", round(f1_score(y_test, y_pred, average='weighted'), 4))
print(classification_report(y_test, y_pred))

joblib.dump(model, r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")
print("Model saved!")