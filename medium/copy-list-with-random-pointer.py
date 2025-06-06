# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        head2 = Node(head.val)
        trav = head
        trav2 = head2
        node_mapper = { trav: trav2 }
        while trav:
            if trav.next:
                new_node = Node(trav.next.val)
                trav2.next = new_node
                trav2 = trav2.next
            else:
                trav2.next = None
            trav = trav.next
            node_mapper[trav] = trav2

        
        trav = head
        trav2 = head2
        while trav:
            if trav.random:
                trav2.random = node_mapper[trav.random]
            trav = trav.next
            trav2 = trav2.next
        return head2



        
        
