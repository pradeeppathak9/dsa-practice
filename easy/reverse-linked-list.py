# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solution(head):
    curr = head
    previous = None
    while curr:
        curr_next = curr.next
        curr.next = previous
        previous = curr
        curr = curr_next
    return previous



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return solution(head)
        
