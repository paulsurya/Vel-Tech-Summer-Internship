import numpy as np

marks = np.array([98, 85, 76, 90, 89, 95, 92, 88, 91, 94])

print("\t=====Marks Report=====")
print("Marks:\t\t\t", marks)
print("Mean:\t\t\t", np.mean(marks))
print("Highest Mark:\t\t", np.max(marks))
print("Lowest Mark:\t\t", np.min(marks))
print("Standard Deviation:\t", np.std(marks))
print("Students who passed:\t", np.sum(marks >= 50))