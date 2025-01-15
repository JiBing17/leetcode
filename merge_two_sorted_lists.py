# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # node used to start new linked list (used for traversal and linking)
        curr = ListNode(None, None)
        # another pointer to return head of new list (doesn't move)
        dummy = curr

        # keep attaching nodes until one is is empty 
        while list1 and list2:

            # attach node from list 1 to new list
            if list1.val <= list2.val:
                curr.next = list1 # attach
                list1 = list1.next # go to next node in list1
            else: # same case but when val in list2 is smaller
                curr.next = list2
                list2 = list2.next

            curr = curr.next # move current pointer of new list for next attachment

        while list1: # keep attaching rest of list1 if not empty 
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        while list2: # same as above but for list2
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        return dummy.next # return head of the new list

        