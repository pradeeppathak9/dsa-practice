# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseNodes(head):
            curr = head
            previous = None
            while curr:
                curr_next = curr.next
                curr.next = previous
                previous = curr
                curr = curr_next
            return previous

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.get_Kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reversing group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next


    def get_Kth(self, curr, k):
        while curr and k > 0: 
            curr = curr.next
            k -= 1
        return curr

        

        


        


