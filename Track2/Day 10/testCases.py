import pandas as pd
from predict import predict

def predict_safe(inputs):
    try:
        return predict(inputs)
    except Exception as e:
        return {'signal': 'Error', 'confidence': 'N/A', 'strength': 'N/A', 'error': str(e)}

test_cases = [
    {'rsi': 30.0, 'ma_cross':  5.2, 'volatility': 10.1, 'volume_ratio': 1.8, 'vwap_diff':  2.1, 'daily_range':  6.5, 'delivery_pct': 0.60},
    {'rsi': 35.0, 'ma_cross':  3.0, 'volatility':  8.5, 'volume_ratio': 1.5, 'vwap_diff':  1.2, 'daily_range':  5.0, 'delivery_pct': 0.55},
    {'rsi': 50.0, 'ma_cross':  0.5, 'volatility':  5.2, 'volume_ratio': 1.0, 'vwap_diff':  0.1, 'daily_range':  3.0, 'delivery_pct': 0.50},
    {'rsi': 78.0, 'ma_cross': -8.3, 'volatility': 18.5, 'volume_ratio': 0.6, 'vwap_diff': -3.2, 'daily_range': 12.0, 'delivery_pct': 0.30},
    {'rsi': 85.0, 'ma_cross':-12.0, 'volatility': 25.0, 'volume_ratio': 0.3, 'vwap_diff': -5.0, 'daily_range': 20.0, 'delivery_pct': 0.20},
    {'rsi':  0.0, 'ma_cross':  0.0, 'volatility':  0.0, 'volume_ratio': 0.0, 'vwap_diff':  0.0, 'daily_range':  0.0, 'delivery_pct': 0.00},
    {'rsi':100.0, 'ma_cross': 50.0, 'volatility':100.0, 'volume_ratio':10.0, 'vwap_diff': 50.0, 'daily_range':100.0, 'delivery_pct': 1.00},
    {'rsi': 28.0, 'ma_cross':  5.2, 'volatility': 10.1, 'volume_ratio': 1.8, 'vwap_diff':  2.1, 'daily_range':  6.5, 'delivery_pct': 0.60},
    {'rsi': 72.0, 'ma_cross': -6.0, 'volatility': 15.0, 'volume_ratio': 0.5, 'vwap_diff': -2.5, 'daily_range': 10.0, 'delivery_pct': 0.25},
    {'rsi': -99, 'ma_cross': None,  'volatility': -5.0, 'volume_ratio': 1.0, 'vwap_diff':  0.0, 'daily_range':  3.0, 'delivery_pct': 0.50},
]

labels = [
    "Normal  — Oversold bullish",
    "Normal  — Mild upward trend",
    "Normal  — Neutral market",
    "High Risk — Overbought bearish",
    "High Risk — Extreme bearish",
    "Edge    — All minimum values",
    "Edge    — All maximum values",
    "Known   — Strong buy signal",
    "Known   — Strong sell signal",
    "Invalid — Bad input",
]

results = []
for i, (case, label) in enumerate(zip(test_cases, labels), 1):
    result = predict_safe(case)
    results.append({
        'Case'      : i,
        'Type'      : label,
        'Signal'    : result.get('signal', 'Error'),
        'Confidence': result.get('confidence', 'N/A'),
        'Strength'  : result.get('strength', 'N/A'),
        'Status'    : 'PASS' if result.get('signal') != 'Error' else 'ERROR'
    })

log_df = pd.DataFrame(results)
print(log_df.to_string(index=False))