#(Homework) Question 2
#Read binary number from the user
binary_str = input("Enter a binary number: ")
try:
    # Convert binary to decimal using int with base 2
    decimal_value = int(binary_str, 2)
    #Display the result
    print("The decimal equivalent of binary", binary_str, "is", decimal_value)
    #Except message if input number is wrong
except ValueError:
        print("wrong binary number. Please enter a valid binary number.")