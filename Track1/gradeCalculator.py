def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 45:
        return "D"
    else:
        return "F"


def main():
    marks = list()
    for i in range(5):
        mark = int(input(f"Enter mark for subject{i + 1}: "))
        marks.append(mark)

    grades = [get_grade(mark) for mark in marks]

    for i in range(5):
        print(f"\n\nThe grade for subject{i + 1} is {grades[i]}")


if __name__ == "__main__":
    main()
