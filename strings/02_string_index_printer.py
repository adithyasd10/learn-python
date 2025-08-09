# This program takes a string as input and:
# 1. Prints its characters from left to right, separated by spaces.
# 2. Prints the index positions of the characters in reverse order.
#
# Example:
# Input:
# Enter a string: hello
#
# Output:
# h e l l o 
# 4 3 2 1 0
#
# How to run:
# 1. Save this file as string_index_printer.py
# 2. Run using:
#       python string_index_printer.py
# 3. Enter any string when prompted to see its characters and reverse indices.

s = input('Enter a string: ')
for i in range(len(s)):
    print(s[i], end=" ")
print("")
for i in range(len(s) - 1, -1, -1):
    print(i, end=" ")
