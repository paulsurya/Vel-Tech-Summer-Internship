import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv('./datasets/student-mat.csv', sep=';')

# Select the single best feature (G1) and the target (G3)
X = df[['G1']]
y = df['G3']

# Split the data standardly (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file using pickle
# 'wb' means "write binary" mode
with open('./models/best_student_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("SUCCESS: Model saved as 'best_student_model.pkl'!")
