# (Homework) Question1-B
# Solving by the help of math library
import math

# Reading the number from the user
number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial don't work for negative numbers.")
else:
    # Calculate the factorial using math.factorial
    result = math.factorial(number)
    # Display the result
    print(f"The factorial of {number} is {result}")