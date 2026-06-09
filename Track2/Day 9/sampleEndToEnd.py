import joblib
import pandas as pd

model = joblib.load(r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")

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

samples = [
    {'rsi': 28.0, 'ma_cross': 5.2, 'volatility': 10.1, 'volume_ratio': 1.8, 'vwap_diff': 2.1, 'daily_range': 6.5, 'delivery_pct': 0.60},
    {'rsi': 78.0, 'ma_cross': -8.3, 'volatility': 18.5, 'volume_ratio': 0.6, 'vwap_diff': -3.2, 'daily_range': 12.0, 'delivery_pct': 0.30},
    {'rsi': 50.0, 'ma_cross': 0.5, 'volatility': 5.2, 'volume_ratio': 1.0, 'vwap_diff': 0.1, 'daily_range': 3.0, 'delivery_pct': 0.50},
    {'rsi': 62.0, 'ma_cross': 12.0, 'volatility': 22.0, 'volume_ratio': 3.5, 'vwap_diff': 4.0, 'daily_range': 18.0, 'delivery_pct': 0.75},
    {'rsi': 38.0, 'ma_cross': -5.0, 'volatility': 8.0, 'volume_ratio': 0.4, 'vwap_diff': -2.0, 'daily_range': 5.0, 'delivery_pct': 0.20},
]

print(f"{'Sample':<10} {'Signal':<20} {'Confidence':<15} {'Strength'}")
print("-" * 65)
for i, sample in enumerate(samples, 1):
    input_df = pd.DataFrame([sample])
    result = enrich_prediction(model, input_df)
    print(f"Sample {i:<4} {result['signal']:<20} {result['confidence']:<15} {result['strength']}")