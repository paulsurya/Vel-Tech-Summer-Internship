import joblib
import os
import numpy as np
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from sklearn.model_selection import train_test_split
import glob

os.makedirs('models', exist_ok=True)

model = joblib.load(r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")

joblib.dump(model, 'models/final_model.pkl')
print("final_model.pkl saved.")

loaded_model = joblib.load('models/final_model.pkl')
print("Load test passed.")
print("Model type     :", type(loaded_model))
print("Features       :", loaded_model.feature_names_in_)
print("Num features   :", len(loaded_model.feature_names_in_))

sample = pd.DataFrame([{
    'rsi': 45.0,
    'ma_cross': -2.5,
    'volatility': 12.3,
    'volume_ratio': 1.1,
    'vwap_diff': -0.5,
    'daily_range': 8.0,
    'delivery_pct': 0.45
}])

pred = loaded_model.predict(sample)
print("Sample prediction:", pred[0], "→", "Buy" if pred[0] == 1 else "Sell / Stay Out")