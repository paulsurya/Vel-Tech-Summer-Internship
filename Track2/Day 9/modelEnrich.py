import joblib
import numpy as np
import pandas as pd

model = joblib.load(r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")
sample = pd.DataFrame([{
    'rsi': 45.0,
    'ma_cross': -2.5,
    'volatility': 12.3,
    'volume_ratio': 1.1,
    'vwap_diff': -0.5,
    'daily_range': 8.0,
    'delivery_pct': 0.45
}])

def enrich_prediction(model, input_df):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    confidence = max(probability) * 100

    if prediction == 1:
        signal = "Buy"
        advice = "Model suggests upward movement tomorrow. Consider entering a position."
    else:
        signal = "Sell / Stay Out"
        advice = "Model suggests downward movement tomorrow. Consider avoiding or exiting."

    if confidence >= 70:
        strength = "Strong Signal"
    elif confidence >= 55:
        strength = "Moderate Signal"
    else:
        strength = "Weak Signal"

    return {
        'signal': signal,
        'confidence': f"{confidence:.1f}%",
        'strength': strength,
        'advice': advice
    }

result = enrich_prediction(model, sample)
print("Signal     :", result['signal'])
print("Confidence :", result['confidence'])
print("Strength   :", result['strength'])
print("Advice     :", result['advice'])