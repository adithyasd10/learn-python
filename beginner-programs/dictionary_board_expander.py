# This program demonstrates the use of a dictionary (hashmap) to map abbreviations to their full forms.
# It defines a dictionary `dict1` with abbreviations as keys and their expanded forms as values.
# A list `list1` contains common education board abbreviations.
# The program loops through each abbreviation in the list and prints each character along with its meaning.
# 
# Special Case:
# For the second abbreviation in the list (`CBSE`), the letter 'C' is mapped to 'Central' instead of 'Certificate'.
#
# Example Output:
# I-Indian
# C-Certificate
# S-Secondary
# E-Education
# ===============
# C-Central
# B-Board
# S-Secondary
# E-Education
# ===============
# H-Higher
# S-Secondary
# E-Education
# ===============
#
# How to run:
# 1. Save this file as board_abbreviation_expander.py
# 2. Run in terminal using:
#       python board_abbreviation_expander.py

# dictionary/hashmap
dict1 = {
    'I': 'Indian',
    'C': 'Certificate',
    'S': 'Secondary',
    'E': 'Education',
    'C1': 'Central',
    'B': 'Board',
    'H': 'Higher'
}

list1 = ['ICSE', 'CBSE', 'HSE']

for i in list1:
    for j in i:
        print(j, end='-')
        if i == list1[1] and j == 'C':
            print(dict1['C1'])  # Special case for 'CBSE'
        else:
            print(dict1[j])
    print('===============')
