import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the data
df = pd.read_csv('./datasets/student-mat.csv', sep=';')

# Select Features (X) and Target (y)
feature_columns = ['studytime', 'failures', 'absences', 'G1', 'G2']
X = df[feature_columns]
y = df['G3']

# Setup our fake student as a small DataFrame with matching column names
# (This stops the warning message from showing up!)
fake_student = pd.DataFrame([[4, 0, 2, 15, 16]], columns=feature_columns)


# =====================================================================
# RUN 1: Test Size = 0.1 (10% Test, 90% Train)
# =====================================================================
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.1, random_state=42)

model1 = LinearRegression()
model1.fit(X_train1, y_train1)

predictions1 = model1.predict(X_test1)
mae1 = mean_absolute_error(y_test1, predictions1)
r2_1 = r2_score(y_test1, predictions1)
fake_pred1 = model1.predict(fake_student)

print("=== RESULTS FOR TEST SIZE 0.1 ===")
print("Average Error (MAE):", round(mae1, 2))
print("Model Accuracy (R2):", round(r2_1, 2))
print("Fake Student Prediction:", round(fake_pred1[0], 2))
print("-" * 40)


# =====================================================================
# RUN 2: Test Size = 0.2 (20% Test, 80% Train)
# =====================================================================
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X_train2, y_train2)

predictions2 = model2.predict(X_test2)
mae2 = mean_absolute_error(y_test2, predictions2)
r2_2 = r2_score(y_test2, predictions2)
fake_pred2 = model2.predict(fake_student)

print("=== RESULTS FOR TEST SIZE 0.2 ===")
print("Average Error (MAE):", round(mae2, 2))
print("Model Accuracy (R2):", round(r2_2, 2))
print("Fake Student Prediction:", round(fake_pred2[0], 2))
print("-" * 40)


# =====================================================================
# RUN 3: Test Size = 0.3 (30% Test, 70% Train)
# =====================================================================
X_train3, X_test3, y_train3, y_test3 = train_test_split(X, y, test_size=0.3, random_state=42)

model3 = LinearRegression()
model3.fit(X_train3, y_train3)

predictions3 = model3.predict(X_test3)
mae3 = mean_absolute_error(y_test3, predictions3)
r2_3 = r2_score(y_test3, predictions3)
fake_pred3 = model3.predict(fake_student)

print("=== RESULTS FOR TEST SIZE 0.3 ===")
print("Average Error (MAE):", round(mae3, 2))
print("Model Accuracy (R2):", round(r2_3, 2))
print("Fake Student Prediction:", round(fake_pred3[0], 2))
print("-" * 40)