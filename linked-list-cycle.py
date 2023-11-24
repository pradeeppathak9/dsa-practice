# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def solution(head):
    if not head:
        return
    head1 = head
    head2 = head.next
    while True:
        if head1 == head2:
            return True
        if head1.next: 
            head1 = head1.next
        else:
            break
        if head2.next and head2.next.next:
            head2 = head2.next.next
        else:
            break
    return False
    

        

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return solution(head)
