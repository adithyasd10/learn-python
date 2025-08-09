# This program defines a class Solution with a method romanToInt that converts a Roman numeral string to its integer value.
# It uses a dictionary (romanMap) to map each Roman numeral character to its corresponding integer value.
# The method iterates through the string, checking if the current numeral should be added or subtracted 
# (based on the Roman numeral rules where a smaller numeral before a larger one means subtraction).
#
# Example:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation:
# M  (1000)
# CM (900)   -> 100 less than 1000
# XC (90)    -> 10 less than 100
# IV (4)     -> 1 less than 5
# Total = 1000 + 900 + 90 + 4 = 1994
#
# How to run:
# 1. Save this file as roman_to_integer.py
# 2. Add the following test code at the bottom to run:
#
#     if __name__ == "__main__":
#         s = Solution()
#         print(s.romanToInt("III"))      # Output: 3
#         print(s.romanToInt("LVIII"))    # Output: 58
#         print(s.romanToInt("MCMXCIV"))  # Output: 1994

class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        while i < len(s):
            current_val = romanMap[s[i]]

            if i + 1 < len(s):
                next_val = romanMap[s[i + 1]]

                if current_val < next_val:
                    total += next_val - current_val
                    i += 2
                else:
                    total += current_val
                    i += 1
            else:
                total += current_val
                i += 1

        return total
