# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        
        # two pointers (slow going over 1 node / iteration and fast going 2 nodes / iteration)
        slow, fast = head, head

        while fast != None and fast.next != None: # keep going until fast pointer can't go further (end of list)
            slow = slow.next # slow move
            fast = fast.next.next # fast move
            if slow  == fast: # same node then there is a loop since fast should've became that node earlier (theres a loop)
                return True
        return False # fast pointer ends, return false (no loop)