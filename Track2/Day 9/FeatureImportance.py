import joblib
import matplotlib.pyplot as plt
import pandas as pd

model = joblib.load(r"C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track2\Day 9\tuned_model.pkl")

feature_names = model.feature_names_in_

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=True)

plt.figure(figsize=(8, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Importance Score')
plt.title('Top Features — What the Model Cares About')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()