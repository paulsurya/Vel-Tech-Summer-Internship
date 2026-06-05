import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./dataset/RELIANCE.csv')

df['Volume'] = df['Volume'].replace(0, np.nan).ffill()
df['MA_7'] = df['Close'].rolling(7).mean().fillna(df['Close'].expanding().mean())
df['Price Range'] = df['High'] - df['Low']
df['Daily Return'] = df['Close'].pct_change().fillna(0) * 100
df['Target'] = df['Close'].shift(-1)
df.dropna(inplace=True)

features = ['Open', 'High', 'Low', 'Volume', 'MA_7', 'Price Range', 'Daily Return']

plt.figure(figsize=(8, 5))
sns.histplot(df['Target'], bins=30, color='steelblue', kde=True)
plt.title('distribution of target (next day close price)')
plt.xlabel('price')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('./charts/target_distribution.png')
plt.close()
print("saved target_distribution.png")

correlations = df[features].corrwith(df['Target']).abs().sort_values(ascending=False)
top_features = correlations.head(4).index.tolist()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, feature in enumerate(top_features):
    axes[i].scatter(df[feature], df['Target'], alpha=0.4, color='steelblue', s=15)
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('target')
    axes[i].set_title(f'{feature} vs target')

plt.suptitle('top features vs target', fontsize=13)
plt.tight_layout()
plt.savefig('./charts/top_features_vs_target.png')
plt.close()
print("saved top_features_vs_target.png")

plt.figure(figsize=(8, 6))
corr_matrix = df[features + ['Target']].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('correlation heatmap')
plt.tight_layout()
plt.savefig('./charts/correlation_heatmap.png')
plt.close()
print("saved correlation_heatmap.png")

print("\nall 3 plots saved successfully!")