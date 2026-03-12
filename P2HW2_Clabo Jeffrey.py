# Jeffrey Clabo
 # 3/12/2026
 # P2HW2
 # GRADE CALCULATOR


# Initialize an empty list to store grades
grades = []

# Input grades for 6 modules
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

# Calculate results
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# Print results
print("\\n-----------Results-----------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_of_grades}")
print(f"Average: {average:.2f}")
print("------------------------------")