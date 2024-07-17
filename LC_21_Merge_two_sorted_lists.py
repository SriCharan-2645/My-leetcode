"""
21. Merge Two Sorted Lists
Easy
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # create a dummy node to start with
        dummy = ListNode()
        tail = dummy # assigning tail as the head of the dummy
        while list1 and list2: # they none of them are not nulls
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # update tail in both cases!
        if list1: # is list1 is not null
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

    # You cannot return `dummy` instead of `dummy.next` because `dummy` is the initial dummy node you created to
    # serve as a placeholder for the merged linked list. It has a default value of `val` equal to 0 and `next` equal
    # to None. Returning `dummy` would include this placeholder node as the head of your merged list, which you don't
    # want.

    # By returning `dummy.next`, you effectively return the actual head of the merged list, which is the first node
    # containing a valid value from either `list1` or `list2`. This gives you the correct merged list without the
    # placeholder node.


