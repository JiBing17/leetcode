# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # null for tail of the linked list
        prev = None
        
        # traverse through from left to right
        while head != None:

            # ref for next node of current head
            next_node = head.next
            # redirect pointer to node behind head
            head.next = prev
            # move prev to the right for next iteration
            prev = head 
            # chage head to next node it pointed to at start
            head = next_node 
        # prev at end will contain the head of the reversed linked list
        return prev

