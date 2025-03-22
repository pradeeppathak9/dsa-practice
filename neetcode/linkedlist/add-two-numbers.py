# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def solution(l1, l2):
    trav = res_root = None
    carry = 0

    while l1 or l2:
        tot = carry
        if l1 is not None:
            tot += l1.val
            l1 = l1.next
        if l2 is not None:
            tot += l2.val
            l2 = l2.next
        carry = 1 if tot > 9 else 0
        tot = tot % 10
        node = ListNode(tot)
        if res_root is None:
            trav = res_root = node
        else:
            trav.next = node
            trav = trav.next
    
    if carry:
        node = ListNode(1)
        trav.next = node
    return res_root


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return solution(l1, l2)
        
