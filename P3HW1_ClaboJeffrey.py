# Jeffrey Clabo
 # 3/27/2026
 # P3HW1
 # GRADE CALCULATOR








def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    grades = []
    
    # Get grades for 6 modules
    for i in range(1, 7):
        grade = float(input(f'Enter grade for Module {i}: '))
        grades.append(grade)
    
    # Calculate results
    lowest_grade = min(grades)
    highest_grade = max(grades)
    sum_of_grades = sum(grades)
    average = sum_of_grades / len(grades)
    
    # Determine letter grade
    letter_grade = calculate_grade(average)

    # Display results
    print("\\n-----------Results-----------")
    print(f"Lowest Grade: {lowest_grade:.1f}")
    print(f"Highest Grade: {highest_grade:.1f}")
    print(f"Sum of Grades: {sum_of_grades:.1f}")
    print(f"Average: {average:.2f}")
    print("-----------------------------")
    print(f"Your grade is: {letter_grade}")

if __name__ == "__main__":
    main()