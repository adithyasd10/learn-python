# This program defines a class Solution with a method isValid that checks if a given string of brackets is valid.
# A string is considered valid if:
# 1. Every opening bracket has a corresponding closing bracket of the same type.
# 2. Brackets are closed in the correct order.
#
# The algorithm uses a stack to store opening brackets and a dictionary (bracket_map)
# to match each closing bracket to its corresponding opening bracket.
#
# Example:
# Input: s = "()"
# Output: True
#
# Input: s = "()[]{}"
# Output: True
#
# Input: s = "(]"
# Output: False
#
# How to run:
# 1. Save this file as valid_parentheses.py
# 2. Add the following test code at the bottom:
#
#     if __name__ == "__main__":
#         s = Solution()
#         print(s.isValid("()"))        # Output: True
#         print(s.isValid("()[]{}"))    # Output: True
#         print(s.isValid("(]"))        # Output: False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
