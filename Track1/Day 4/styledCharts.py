import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./datasets/student-mat.csv', sep=';')

# Convert the grade column to a number standardly
df['G3'] = pd.to_numeric(df['G3'], errors='coerce')

# Separate the rows by study time manually (1 to 4)
group1 = df[df['studytime'] == 1]
group2 = df[df['studytime'] == 2]
group3 = df[df['studytime'] == 3]
group4 = df[df['studytime'] == 4]

# Calculate the average grade for each group
avg1 = group1['G3'].mean()
avg2 = group2['G3'].mean()
avg3 = group3['G3'].mean()
avg4 = group4['G3'].mean()

# Calculate the overall average grade
overall_mean = df['G3'].mean()

# Make simple lists for the chart data
x_labels = ['<2 hrs', '2–5 hrs', '5–10 hrs', '>10 hrs']
averages = [avg1, avg2, avg3, avg4]

# Create a new separate figure window
plt.figure()

# Plot the bars using basic primary colors
plt.bar(x_labels, averages, color=['blue', 'orange', 'green', 'red'], width=0.5)

# Draw the overall mean line standardly
plt.axhline(overall_mean, color='black', linestyle='--', label='Overall mean')

# Add number labels on top of each bar manually
plt.text(0, avg1 + 0.2, str(round(avg1, 2)), ha='center')
plt.text(1, avg2 + 0.2, str(round(avg2, 2)), ha='center')
plt.text(2, avg3 + 0.2, str(round(avg3, 2)), ha='center')
plt.text(3, avg4 + 0.2, str(round(avg4, 2)), ha='center')

# Add titles, labels, and the legend box
plt.title('Average Final Grade (G3) by Weekly Study Time')
plt.xlabel('Weekly Study Time')
plt.ylabel('Average G3 Grade')
plt.ylim(0, 16)
plt.legend()

# Save the picture and display it in a windows popup
plt.savefig('./savedCharts/bar_studytime.png')
print("Saved: bar_studytime.png")
plt.show()