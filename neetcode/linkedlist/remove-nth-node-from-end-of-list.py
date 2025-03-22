# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trav = head
        count = 0
        while trav:
            count += 1
            trav = trav.next

        if n <= count:
            count = count - n
            if count == 0:
                head = head.next
            else:
                trav = head
                count -= 1
                while count:
                    trav = trav.next
                    count -= 1
                trav.next = trav.next.next
        
        return head 

        

        
