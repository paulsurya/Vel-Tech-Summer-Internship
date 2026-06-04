import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data from your local folder
df = pd.read_csv('./datasets/student-mat.csv', sep=';')

# List of single features to try
features_to_test = ['studytime', 'failures', 'absences', 'G1']
target = 'G3'

# We will save the RMSE score of each feature here to compare them later
rmse_results = {}

print("=== TRAINING 4 SEPARATE MODELS ===")

# Loop through each single feature one by one
for col in features_to_test:
    # Select just this one feature column
    X = df[[col]]  # Double brackets keeps it as a DataFrame
    y = df[target]
    
    # Split the data standardly (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the single-feature model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict and calculate RMSE
    predictions = model.predict(X_test)
    
    # RMSE is just the square root of Mean Squared Error
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    
    # Save the score in our dictionary
    rmse_results[col] = rmse
    print(f"Model using ONLY '{col}' -> RMSE: {round(rmse, 2)}")

print("-" * 50)

# Find which feature has the lowest error (best score)
best_feature = min(rmse_results, key=rmse_results.get)
print(f"🏆 WINNER: The single best predictor is '{best_feature}' with the lowest RMSE of {round(rmse_results[best_feature], 2)}")
print("-" * 50)


# =====================================================================
# RANDOM STUDENT TEST USING THE BEST SINGLE FEATURE
# =====================================================================
print("=== RANDOM STUDENT TEST (Using Best Feature) ===")

# Re-split using only the winning best feature
X_best = df[[best_feature]]
y_best = df[target]
X_train, X_test, y_train, y_test = train_test_split(X_best, y_best, test_size=0.2, random_state=42)

# Re-train the winning model
best_model = LinearRegression()
best_model.fit(X_train, y_train)

# Pick a random student from the test dataset
random_student_features = X_test.sample(1, random_state=10)
student_index = random_student_features.index[0]

# Get the real grade and make the single-feature prediction
real_grade = y_test.loc[student_index]
predicted_grade = best_model.predict(random_student_features)

print(f"Student's value for '{best_feature}':", random_student_features.values[0][0])
print("Predicted Grade by Model:", round(predicted_grade[0], 2))
print("Correct (Actual) Grade:  ", real_grade)

