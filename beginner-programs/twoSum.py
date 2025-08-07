# This program defines a class Solution with a method twoSum that takes a list of numbers (nums) and a target number.
# It returns the indices of the two numbers in the list that add up to the target.
# The method uses a dictionary (hash map) to store previously seen numbers for efficient lookup.
# 
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  # Because nums[0] + nums[1] == 2 + 7 == 9
#
# How to run:
# 1. Save this file as two_sum.py
# 2. Add the following test code at the bottom of the file to see output:
#
#     if __name__ == "__main__":
#         s = Solution()
#         print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []
