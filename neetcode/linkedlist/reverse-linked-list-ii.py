# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        dummy = ListNode(0, head)
        groupPrev = self.get_kth(dummy, left - 1) 
        kth = self.get_kth(dummy, right) 
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

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        
