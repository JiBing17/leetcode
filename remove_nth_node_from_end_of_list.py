# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        


        # used to reference head of list at end
        dummy = ListNode(0)
        dummy.next = head

        # have a left pointer point to node before starting node
        left = dummy

        # have right pointer move n spaces (should be n+1 nodes apart from left pointer)
        right = head
        for i in range(n):
            right = right.next
        
        # keep moving both pointers until right pointer points to None
        while right:
            right = right.next
            left = left.next
        
        # left pointer should be at the node before the nth last node so change next pointer to the node after it's next node
        left.next = left.next.next

        return dummy.next # return head 