import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv('./datasets/student-mat.csv', sep=';')

# Select the single best feature (G1) and target (G3)
X = df[['G1']]
y = df['G3']

# Split into training and testing pools standardly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions for the entire test dataset
predictions = model.predict(X_test)

# =====================================================================
# CREATE THE SCATTER PLOT
# =====================================================================
plt.figure(figsize=(6, 6))

# Plot actual vs predicted grades as blue dots
plt.scatter(y_test, predictions, color='blue', alpha=0.6, label='Predicted vs Actual')

# Define the coordinates for a perfect diagonal line (from 0 to 20 on both axes)
perfect_line_x = [0, 20]
perfect_line_y = [0, 20]

# Plot the red diagonal line representing 100% perfect predictions
plt.plot(perfect_line_x, perfect_line_y, color='red', linestyle='--', linewidth=2, label='Perfect Predictions (y = x)')

# Add standard labels, limits, and legend
plt.title('Actual G3 Grades vs. Predicted G3 Grades')
plt.xlabel('Actual G3 Grades')
plt.ylabel('Predicted G3 Grades')
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Display the window
plt.show()