#Jeffrey Clabo 
#4/29/2026
#P5LAB_ClaboJeffrey
#Change calculator


import random

def disperse_change(change):
    # Calculate the number of each coin type
    dollars = int(change)
    change -= dollars
    quarters = int(change // 0.25)
    change -= quarters * 0.25
    dimes = int(change // 0.10)
    change -= dimes * 0.10
    nickels = int(change // 0.05)
    change -= nickels * 0.05
    pennies = round(change / 0.01)

    # Display the change breakdown
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")

    # Prompt user for cash input
    cash_entered = float(input("Enter the amount of cash you will put into the self-checkout: $"))

    # Calculate change
    change_owed = round(cash_entered - total_owed, 2)

    if change_owed < 0:
        print("Insufficient funds. Please enter a valid amount.")
    else:
        print(f"Change owed: ${change_owed}")
        disperse_change(change_owed)

if __name__ == "__main__":
    main()
