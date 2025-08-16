# strStr implementation
# Problem: Given two strings haystack and needle, return the index of the first
# occurrence of needle in haystack. If needle is not part of haystack, return -1.
#
# Example:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and again at 6. The first occurrence is at 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Python's built-in find() handles this efficiently
        return haystack.find(needle)
