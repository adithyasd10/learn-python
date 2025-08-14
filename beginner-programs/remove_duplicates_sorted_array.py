# This program removes duplicates from a sorted array in-place and returns the number of unique elements.
# It uses the two-pointer technique:
# - Pointer i tracks the position of the last unique element.
# - Pointer j scans through the array, looking for new unique values.
# When a new unique value is found, i is incremented and updated with nums[j].
#
# Example:
# Input:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output:
# Unique count = 5
# nums after operation = [0, 1, 2, 3, 4, ...]  # The rest can be ignored
#
# How to run:
# 1. Save this as remove_duplicates_sorted_array.py
# 2. Add a test:
#
#     if __name__ == "__main__":
#         nums = [0,0,1,1,1,2,2,3,3,4]
#         s = Solution()
#         k = s.removeDuplicates(nums)
#         print("Unique count:", k)
#         print("Array after removal:", nums[:k])

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
