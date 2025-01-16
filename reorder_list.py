# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """'

        # find head node of second half if split using fast and slow pointers
        fast, slow, start = head.next, head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next # head of second list
        slow.next, prev = None, None # end first list by connect next pointer to None 

        # reverse second list 
        while second:
            second_next = second.next
            second.next = prev
            prev = second
            second = second_next
        
        # start connect the nodes from left to right for both lists (L_0, L_N ... )
        while prev and start:

            # ref to each head's next pointers
            start_next = start.next 
            prev_next = prev.next

            # have head of first point to head of second
            start.next = prev
            start = start_next # change head of first to node to the right of it

            prev.next = start # have head of second list point to new head of first
            prev = prev_next # change head of second to node on the right of it