# This program defines a class Solution with a method mergeTwoLists that merges two sorted singly linked lists
# into a single sorted linked list.
#
# The algorithm uses a dummy node and a tail pointer to build the merged list.
# It compares nodes from both lists one by one, attaching the smaller node to the result list,
# until one of the lists is exhausted. Then it attaches the remaining nodes from the other list.
#
# Example:
# Input:
# list1 = 1 -> 2 -> 4
# list2 = 1 -> 3 -> 4
# Output:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4
#
# How to run:
# 1. Save this file as merge_two_sorted_lists.py
# 2. Add the following test code at the bottom:
#
#     if __name__ == "__main__":
#         # Create first linked list: 1 -> 2 -> 4
#         l1 = ListNode(1, ListNode(2, ListNode(4)))
#         # Create second linked list: 1 -> 3 -> 4
#         l2 = ListNode(1, ListNode(3, ListNode(4)))
#
#         s = Solution()
#         merged = s.mergeTwoLists(l1, l2)
#
#         # Print merged linked list
#         while merged:
#             print(merged.val, end=" -> " if merged.next else "\n")
#             merged = merged.next

from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
