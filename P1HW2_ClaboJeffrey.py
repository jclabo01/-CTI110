# Jeffrey Clabo
 # 2/17/2026
 # P1HW2
 # Calculate and display travel expenses

# Step 1: Ask user to enter their budget
budget = float(input("Enter your budget: "))

# Step 2: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Step 4: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Step 5: Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Step 6: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 8: Display results
print(f"Travel Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")