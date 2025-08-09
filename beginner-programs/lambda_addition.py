# This program demonstrates the use of a lambda function in Python to add two numbers.
# A lambda function is an anonymous, single-line function defined using the 'lambda' keyword.
# The program takes two integers as input, uses a lambda function to add them, and prints the result.
#
# Example:
# Input:
# Enter first number: 5
# Enter second number: 7
# Output:
# 12
#
# How to run:
# 1. Save this file as lambda_addition.py
# 2. Run in terminal using:
#       python lambda_addition.py
# 3. Enter two integers when prompted, and the program will display their sum.

# using lambda
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
ladd = lambda n1, n2: n1 + n2
print(ladd(a, b))
