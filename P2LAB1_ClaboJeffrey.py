 # Jeffrey Clabo
 # 2/17/2026
 # P2LAB1
 # Circle Formulas



import math

# Get the radius from the user
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results with specified formatting
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")