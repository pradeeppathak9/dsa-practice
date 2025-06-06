# https://leetcode.com/problems/merge-k-sorted-lists/

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
        
