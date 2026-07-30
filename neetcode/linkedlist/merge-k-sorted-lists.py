# https://leetcode.com/problems/merge-k-sorted-lists/

########## Version 0 (Best)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # Push the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            
        return dummy.next


########## Version 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            head = tail = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    tail = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    tail = list2
                    list2 = list2.next
            if list1:
                tail.next = list1 
            if list2:
                tail.next = list2
            return head.next
            
        if len(lists) == 0:
            return None
        list1 = lists[0]
        for list2 in lists[1:]:
            list1 = mergeTwoLists(list1, list2) 
        return list1
        
