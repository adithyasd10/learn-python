# This program defines a class Solution with a method isPalindrome that checks whether a given number is a palindrome.
# A number is a palindrome if it reads the same forwards and backwards.
# The function prints the digits from left to right and right to left, shows the original and reversed number,
# and prints whether it is a palindrome or not.
#
# Example:
# Input: num = 121
# Output:
# From L to R:
# 1 2 1 
# From R to L:
# 1 2 1 
#
# Original Number: 121
# Reversed Number: 121
# 121 is a palindrome
#
# How to run:
# 1. Save this file as is_palindrome.py
# 2. Add the following test code at the bottom to run:
#
#     if __name__ == "__main__":
#         s = Solution()
#         s.isPalindrome(121)   # Output: True
#         s.isPalindrome(123)   # Output: False

class Solution:
    def isPalindrome(self, num):
        original_num = num
        rev_num = 0

        print('From L to R:')
        for digit in str(num):
            print(digit, end=' ')
        print()

        print('From R to L:')
        for digit in str(num)[::-1]:
            print(digit, end=' ')
        print()

        temp = num
        while temp > 0:
            digit = temp % 10
            rev_num = rev_num * 10 + digit
            temp //= 10

        print(f"\nOriginal Number: {original_num}")
        print(f"Reversed Number: {rev_num}")

        if original_num == rev_num:
            print(num, 'is a palindrome')
            return True
        else:
            print(num, 'is not a palindrome')
            return False
