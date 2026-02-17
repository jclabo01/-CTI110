# Jeffrey Clabo
 # 2/17/2026
 # P1HW1
 # Calculating Exponants 

# ----Calculating Exponents----

def calculate_exponent():
    print("----Calculating Exponents----")
    base = int(input("Enter an integer as the base value: "))
    exponent = int(input("Enter an integer as the exponent: "))
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is {result} !!")

# ----Addition and Subtraction----

def addition_and_subtraction():
    print("----Addition and Subtraction----")
    starting_integer = int(input("Enter a starting integer: "))
    add_integer = int(input("Enter an integer to add: "))
    subtract_integer = int(input("Enter an integer to subtract: "))
    
    result = starting_integer + add_integer - subtract_integer
    print(f"{starting_integer} + {add_integer} - {subtract_integer} is equal to {result}")

# Main function to run both calculations
def main():
    calculate_exponent()
    addition_and_subtraction()

# Run the program
if __name__ == "__main__":
    main()