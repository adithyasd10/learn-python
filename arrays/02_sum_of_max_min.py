# -----------------------------------------------------------------------------
# Program to find the sum of maximum and minimum elements in an array
# Using manual approach (without built-in max/min)
from array import *

def sumof(s):
    n = len(s)

    if n == 1:
        return s[0] * 2  
    else:
        maximum = s[0]
        minimum = s[0]

        for i in range(1, n):
            if s[i] > maximum:
                maximum = s[i]
            if s[i] < minimum:
                minimum = s[i]

        result = maximum + minimum
        return result


s = list(map(int, input('Enter the elements (space-separated): ').split()))
result = sumof(s)
print("Sum of max and min elements:", result)

# -----------------------------------------------------------------------------
# Same logic using built-in max() and min() functions (simpler version)

def sumof_builtin(s):
    return max(s) + min(s)

s = list(map(int, input('\nEnter elements again (for built-in version): ').split()))
result = sumof_builtin(s)
print('Sum of max and min elements (using built-in):', result)

# -----------------------------------------------------------------------------
# Sample Output:
# Enter the elements (space-separated): 2 5 1 8 3
# Sum of max and min elements: 9
#
# Enter elements again (for built-in version): 2 5 1 8 3
# Sum of max and min elements (using built-in): 9
# -----------------------------------------------------------------------------
