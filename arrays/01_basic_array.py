# -----------------------------------------------------------------------------
# Simple basic array using Python's array module
from array import *

vals = array('i', [1, 2, 3, 4, 5])
print("Array with typecode:", vals)

# Output:
# array('i', [1, 2, 3, 4, 5])
# -----------------------------------------------------------------------------
# Accessing elements using index with range
print("\nAccessing elements with range():")
for i in range(len(vals)):
    print(vals[i], end=' ')

# Output:
# 1 2 3 4 5
# -----------------------------------------------------------------------------
# Accessing without using range (using for-each loop)
print("\n\nReversed array using reverse():")
vals.reverse()
for i in vals:
    print(i, end=' ')

# Output:
# 5 4 3 2 1
# -----------------------------------------------------------------------------
# Cloning the array using typecode (for-each loop)
print("\n\nCloning the array (for-each loop):")
vals = array('i', [1, 2, 3, 4, 5])
newArray = array(vals.typecode, (a for a in vals))

print("Old Array:")
for i in vals:
    print(i, end=' ')

print("\nNew Array:")
for i in newArray:
    print(i, end=' ')

# Output:
# Old Array: 1 2 3 4 5
# New Array: 1 2 3 4 5
# -----------------------------------------------------------------------------
# Cloning the array using while loop
print("\n\nCloning the array (while loop):")
vals = array('i', [1, 2, 3, 4, 5])
newArray = array(vals.typecode, (a for a in vals))

i = 0
print("Old Array:")
while i < len(vals):
    print(vals[i], end=' ')
    i += 1

i = 0
print("\nNew Array:")
while i < len(newArray):
    print(newArray[i], end=' ')
    i += 1

# Output:
# Old Array: 1 2 3 4 5
# New Array: 1 2 3 4 5
