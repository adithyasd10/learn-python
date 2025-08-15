# This program removes all occurrences of a given value (val) from an array in-place
# and returns the number of elements that are not equal to val.
#
# Algorithm:
# - Pointer i tracks the position to insert the next "kept" element.
# - Pointer j scans through the array.
# - If nums[j] is not equal to val, it's copied to nums[i], and i is incremented.
# - This overwrites unwanted elements and keeps the rest compacted at the start.
#
# Example:
# Input:
# nums = [3, 2, 2, 3], val = 3
# Output:
# New length = 2
# Array after operation = [2, 2, ...]  # Rest can be ignored
#
# How to run:
# 1. Save this as remove_element_inplace.py
# 2. Add a test:
#
#     if __name__ == "__main__":
#         nums = [3, 2, 2, 3]
#         s = Solution()
#         k = s.removeElement(nums, 3)
#         print("New length:", k)
#         print("Array after removal:", nums[:k])

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
