# Jeffrey Clabo
 # 4/8/2026
 # P4HW2
 # pay statement







def calculate_pay():
    overtime_threshold = 40  # Overtime starts after 40 hours
    overtime_multiplier = 1.5  # Overtime is paid at 1.5 times the regular rate

    total_regular_pay = 0
    total_overtime_pay = 0
    total_gross_pay = 0
    employee_count = 0

    while True:
        employee_name = input("Enter employee's name or 'Done' to terminate: ")
        if employee_name.lower() == "done":
            break

        try:
            hours_worked = float(input(f"How many hours did {employee_name} work? "))
            pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

            if hours_worked > overtime_threshold:
                regular_hours = overtime_threshold
                overtime_hours = hours_worked - overtime_threshold
            else:
                regular_hours = hours_worked
                overtime_hours = 0

            regular_pay = regular_hours * pay_rate
            overtime_pay = overtime_hours * pay_rate * overtime_multiplier
            gross_pay = regular_pay + overtime_pay

            # Accumulate totals
            total_regular_pay += regular_pay
            total_overtime_pay += overtime_pay
            total_gross_pay += gross_pay
            employee_count += 1

            # Display current employee's pay details
            print(f"\\nEmployee name: {employee_name}")
            print(f"Hours Worked: {hours_worked:.1f}   Pay Rate: {pay_rate:.2f}   OverTime: {overtime_hours:.1f}   OverTime Pay: {overtime_pay:.2f}")
            print(f"----------------------------------------------")
            print(f"RegHour Pay: {regular_pay:.2f}   Gross Pay: {gross_pay:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values for hours and pay rate.")
            continue

    # Display summary after user is done
    print(f"Total number of employees entered: {employee_count}")
    print(f"Total amount paid for overtime: {total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: {total_regular_pay:.2f}")
    print(f"Total amount paid in gross: {total_gross_pay:.2f}")

# Run the function to calculate pay
calculate_pay()