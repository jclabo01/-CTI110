# Jeffrey Clabo
 # 3/27/2026
 # P3HW2
 # pay statement





def calculate_pay(hours_worked, pay_rate):
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = hours_worked - overtime_hours
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    return overtime_hours, overtime_pay, regular_pay, gross_pay

def main():
    # Input employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    # Calculate pay
    overtime_hours, overtime_pay, regular_pay, gross_pay = calculate_pay(hours_worked, pay_rate)
    
    # Display results
    print("\\n---------------------------------------------")
    print(f"Employee name: {employee_name}")
    print("Hours Worked    Pay Rate     OverTime      OverTime Pay   RegHour Pay   Gross Pay")
    print("-----------------------------------------------------------------------------")
    print(f"{hours_worked:.1f}             {pay_rate:.2f}        {overtime_hours:.1f}        {overtime_pay:.2f}       {regular_pay:.2f}      {gross_pay:.2f}")
    print("-----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()