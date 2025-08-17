# Search Insert Position implementation
# Problem: Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index 
# where it would be if it were inserted in order.
#
# Example:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Explanation: If target exists, return its index. 
# If not, return the position where target should be inserted.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Step 1: Check if the target is already present in the list
        for i, n in enumerate(nums):
            if n == target:
                return i   # Found target at index i

        # Step 2: If not found, find the position where target should be inserted
        for i, n in enumerate(nums):
            if target < n:
                return i   # Insert before this element

        # Step 3: If target is greater than all elements, insert at the end
        return len(nums)
