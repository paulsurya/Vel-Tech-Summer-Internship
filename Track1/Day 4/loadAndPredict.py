import pandas as pd
import pickle

# Load the saved model from the file
# 'rb' means "read binary" mode
with open('./models/best_student_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)  # Fixed here: removed the extra '.pickle'

print("SUCCESS: Loaded 'best_student_model.pkl' into memory.\n")

# Set up 3 different students with different G1 grades
# Student 1: Struggling (G1 = 5)
# Student 2: Average    (G1 = 11)
# Student 3: Excellent  (G1 = 18)
new_data = {
    'G1': [5, 11, 18]
}

# Convert this into a DataFrame so it matches the training format
students_df = pd.DataFrame(new_data)

# Use the loaded model to predict their final grades
predictions = loaded_model.predict(students_df)

# Print out the results for each student
print("=== PREDICTIONS FOR 3 NEW STUDENTS ===")
print("Student 1 (G1 = 5)  -> Predicted Final Grade:", round(predictions[0], 2))
print("Student 2 (G1 = 11) -> Predicted Final Grade:", round(predictions[1], 2))
print("Student 3 (G1 = 18) -> Predicted Final Grade:", round(predictions[2], 2))