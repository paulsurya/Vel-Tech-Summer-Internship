## Model Summary Card

### Project

Stock Market Trend Classifier · Finance

### Algorithm

XGBoost Classifier (XGBClassifier, scale_pos_weight=2.98)

### Dataset

NSE Historical OHLCV Data · 470,000+ rows · Multiple stocks · 7 features

### Final Performance

| Metric              | Score              |
| ------------------- | ------------------ |
| F1-Score (weighted) | 0.5326             |
| Backtest Hit Rate   | 50.2%              |
| Class Balance       | 75% Sell / 25% Buy |

### Input Features (in this exact order)

| Column       | Type  | Example Value |
| ------------ | ----- | ------------- |
| rsi          | float | 45.0          |
| ma_cross     | float | -2.5          |
| volatility   | float | 12.3          |
| volume_ratio | float | 1.1           |
| vwap_diff    | float | -0.5          |
| daily_range  | float | 8.0           |
| delivery_pct | float | 0.45          |

### Required .pkl Files

| File                   | Contents                                             |
| ---------------------- | ---------------------------------------------------- |
| models/final_model.pkl | XGBoost Classifier trained on multi-stock OHLCV data |

### Sample Input

```python
{
    'rsi'         : 45.0,
    'ma_cross'    : -2.5,
    'volatility'  : 12.3,
    'volume_ratio': 1.1,
    'vwap_diff'   : -0.5,
    'daily_range' : 8.0,
    'delivery_pct': 0.45
}
```

### Sample Output

```python
{
    'signal'    : 'Sell / Stay Out',
    'confidence': '58.2%',
    'strength'  : 'Moderate Signal',
    'advice'    : 'Model suggests downward movement tomorrow.'
}
```

### How to Use

```python
from task2_predict import predict
result = predict(your_input_dict)
```
