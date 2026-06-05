import pickle
import pandas as pd
import numpy as np

loaded_model = pickle.load(open('./models/reliance_model.pkl', 'rb'))

df = pd.read_csv('./dataset/RELIANCE.csv')
df['MA_7'] = df['Close'].rolling(7).mean().fillna(df['Close'].expanding().mean())
df['Price Range'] = df['High'] - df['Low']
df.dropna(inplace=True)

x = df[['Open', 'Close', 'Volume', 'MA_7', 'Price Range']]

predictions = loaded_model.predict(x)
print("predicted next day price:", round(predictions[-1], 2))