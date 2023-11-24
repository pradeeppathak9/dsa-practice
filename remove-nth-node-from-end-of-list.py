# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def solution(head, n):
    
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    count -= n

    prev = None
    curr = head
    while count:
        prev = curr 
        curr = curr.next
        count -= 1
    
    if prev:
        prev.next = curr.next
    else:
        head = curr.next
    return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return solution(head, n)
        
