# Romain Tranchant
# CIS103: Fundamentals of Programming
# 09/12/2024
# Instructor: MD Ali
# Lab 2: Building a Simple Calculator
# Due Date: 09/14/2024 @ 11:59pm
# Take-Home Portion: Enhancing the Calculator


# Define the addition function with 2 numbers by returning
# the sum of these 2 numbers
def addition(num1, num2):
    return num1 + num2

# Define the subtraction function with 2 numbers by returning
# the difference of these 2 numbers
def subtraction(num1, num2):
    return num1 - num2

# Define the multiplication function with 2 numbers by returning
# the product of these 2 numbers
def multiplication(num1, num2):
    return num1 * num2

# Define the division function with 2 numbers by returning
# the quotient of these 2 numbers, except if the second number
# is equal to 0 because a division by 0 is impossible. It would
# return an error message
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error, division by zero impossible"

# Define the exponentiation function with 2 numbers by returning
# num1 to the power of num2
def exponentiation(num1, num2):
    return num1 ** num2

# Define the modulus function with 2 number by returning the
# remainder of num1 divided by num2
def modulus(num1, num2):
    return num1 % num2

# Define the squareroot function by returning the square root
# of num3, except if num3 is a negative number, an error message
# would be returned
def squareroot(num3):
    if num3 >= 0:
        return num3 ** 0.5
    else:
        return "Error, square root of a negative number is not defined in real numbers."

# Define the calculator function
def calculator():

# Start a while loop, to allow the calculator to reset itself until
# the user decides to exit
    while True:

# Prints the choices to the user
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Square root (√)")
        print("8. Exit")

 # Define the variable choice as being the user's input choice
        choice = input("Enter your choice 1, 2, 3, 4, 5, 6, 7 or 8:")

# If the user's choice is not between 1 and 8, print an "Invalid choice"
# message. The continue statement allows the program to process errors and
# invalid inputs, by skipping the rest of the program and resetting the
# calculator
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice! Please enter a valid choice.")
            continue

# The try statement is used to check any errors that might occur during
# the user's inputs of num3
# Call the squareroot function and print the square root of num3, print the
# result,and the continue statement skips the rest of the program to reset
# the calculator7
        try:
            if choice == "7":
                num3 = float(input("Enter your number: "))
                print(f"The result is: {squareroot(num3)}")
                continue

# The valueError handles any format error that the user may input, if the
# user input is not a float number, an "Invalid input! Please enter a number."
# message is shown and the calculator restarts through the continue statement
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

# If the user wants to exit the calculator, print a "Goodbye" message
# and exit the calculator through the break statement
        if choice == "8":
            print("Goodbye!")
            break

# The try statement is used to check any errors that might occur during
# the user's inputs of num1 and num2
        try:

# Ask the user to enter the first number, converts the input from a
# string to a float number, and assigns it to the variable num1
            num1 = float(input("Enter your first number:"))

# Ask the user to enter the second number, converts the input from a
# string to a float number, and assigns it to the variable num2
            num2 = float(input("Enter your second number:"))

# The valueError handles any format error that the user may input, if the
# user input is not a float number, an "Invalid input! Please enter a number."
# message is shown and the calculator restarts through the continue statement
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

# Perform the chosen operation based on user's choice

# Call the addition function and print the sum of num1 and num2
        if choice == "1":
            print(f"The result is: {addition(num1, num2)}")

## Call the subtraction function and print the difference of num1 and num2
        if choice == "2":
            print(f"The result is: {subtraction(num1, num2)}")

# Call the multiplication function and print the product of num1 and num2
        if choice == "3":
            print(f"The result is: {multiplication(num1, num2)}")

# Call the division function and print the quotient of num1 and num2
        if choice == "4":
            print(f"The result is: {division(num1, num2)}")

# Call the division function and print the result of num1 to the power of num2
        if choice == "5":
            print(f"The result is: {exponentiation(num1, num2)}")

# Call the division function and print the remainder of num1 divided num2
        if choice == "6":
            print(f"The result is: {modulus(num1, num2)}")

# This construct ensures that certain code is only executed when the script is run
# directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    calculator()