# Jeffrey Clabo
 # 3/27/2026
 # P3HW2
 # pay statement





def main():
    # Input employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    # Initialize variables
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    gross_pay = 0
    
    # Calculate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        regular_hours = hours_worked
        
    # Calculate regular and overtime pay
    regular_pay = regular_hours * pay_rate
    if overtime_hours > 0:
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Display results
    
    print(f"Employee name: {employee_name}")
    print("Hours Worked    Pay Rate     OverTime      OverTime Pay   RegHour Pay   Gross Pay")
    print("-----------------------------------------------------------------------------")
    print(f"{hours_worked:.1f}             {pay_rate:.2f}        {overtime_hours:.1f}        {overtime_pay:.2f}       {regular_pay:.2f}      {gross_pay:.2f}")
    print("-----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()