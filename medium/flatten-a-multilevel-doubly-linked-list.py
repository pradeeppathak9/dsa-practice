# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            trav = node 
            while trav:
                if trav.child:
                    child_start = trav.child
                    child_end = dfs(trav.child)

                    child_start.prev = trav
                    child_end.next = trav.next

                    child_start.prev.next = child_start
                    if child_end.next:
                        child_end.next.prev = child_end
                    trav.child = None
                if trav.next:
                    trav = trav.next
                else:
                    return trav
        last_node = dfs(head)
        return head
        
