# Jeffrey Clabo
 # 3/9/2026
 # P2LAB2
 # Dictionary

# Creating the dictionary with automobile models and their MPG values
automobile_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Asking the user to enter a vehicle
vehicle = input("Enter a vehicle to see its mpg: ")

# Checking if the vehicle is in the dictionary
if vehicle in automobile_mpg:
    mpg = automobile_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")

    # Asking how many miles they will drive
    miles = float(input(f"How many miles will you drive the {vehicle}? "))
    
    # Calculating gallons of gas needed
    gallons_needed = miles / mpg
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
else:
    print("Vehicle not found in the dictionary.") 