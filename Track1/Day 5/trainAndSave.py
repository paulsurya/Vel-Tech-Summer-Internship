import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('./dataset/RELIANCE.csv')

df['MA_7'] = df['Close'].rolling(7).mean().fillna(df['Close'].expanding().mean())
df['Price Range'] = df['High'] - df['Low']
df['Target'] = df['Close'].shift(-1)
df.dropna(inplace=True)

x = df[['Open', 'Close', 'Volume', 'MA_7', 'Price Range']]
y = df['Target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

pickle.dump(model, open('./models/reliance_model.pkl', 'wb'))
print("model saved!")

y_pred = model.predict(x_test)

print("MAE:", round(mean_absolute_error(y_test, y_pred), 2))
print("R2 Score:", round(r2_score(y_test, y_pred), 4))
print()
print("Actual vs Predicted (first 5):")
for actual, predicted in zip(list(y_test[:5]), y_pred[:5]):
    print(f"  Actual: {round(actual, 2)}  |  Predicted: {round(predicted, 2)}")