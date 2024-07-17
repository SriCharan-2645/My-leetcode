# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # Time: O(n), Memory: O(1)
        slow = head
        fast = head

        # finding second half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None # setting slow.next to None to break the linkedlist.

        # reversing second half
        prev = None
        #curr = brk.next

        while curr:
            nxt = curr.next
            #prev = curr
            curr.next = prev
            prev = curr
            curr = nxt
        start2 = prev # this is the head of linkedlist 2
        # reorder whole list in place
        start1 = head

        while start2: #here since our second LL will always be less than or equal to LL 1, we need to check for exit of LL2
            nxt1 = start1.next
            nxt2 = start2.next
            start1.next = start2
            start2.next = nxt1
            start1 = nxt1
            start2 = nxt2



# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head or not head.next: # checking if list has 0 or 1 Node
#             return

#         # Find the middle of the linked list
#         slow = head
#         fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next

#         # Split the list into two halves
#         second_half = slow.next
#         slow.next = None

#         # Reverse the second half of the list
#         prev = None
#         current = second_half
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node

#         # Merge the two halves of the list
#         first_half = head
#         second_half = prev
#         while second_half:
#             next_node_1 = first_half.next
#             next_node_2 = second_half.next
#             first_half.next = second_half
#             second_half.next = next_node_1
#             first_half = next_node_1
#             second_half = next_node_2
