# This program defines a class Solution with a method longestCommonPrefix that finds
# the longest common prefix string among a list of strings.
# If there is no common prefix, it returns an empty string.
# The algorithm starts with the first string as the prefix and trims it until
# it matches the beginning of all strings in the list.
#
# Example:
# Input: ["flower", "flow", "flight"]
# Output: "fl"
#
# Input: ["dog", "racecar", "car"]
# Output: ""  # No common prefix
#
# How to run:
# 1. Save this file as longest_common_prefix.py
# 2. Add the following test code at the bottom to run:
#
#     if __name__ == "__main__":
#         s = Solution()
#         print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
#         print(s.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
#
# Note: Make sure to import List from typing when running the code.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
