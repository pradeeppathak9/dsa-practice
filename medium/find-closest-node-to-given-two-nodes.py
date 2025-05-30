# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        head, curr_dist = node1, 0
        node1dist = {}
        while not (head == -1 or head in node1dist):
            node1dist[head] = curr_dist
            curr_dist += 1
            head = edges[head]

        node2dist  = {}
        head, curr_dist= node2, 0
        while not (head == -1 or head in node2dist):
            node2dist[head] = curr_dist
            curr_dist += 1
            head = edges[head]

        ans, min_dist = -1, float("inf")
        for node in range(len(edges)):
            if node in node1dist and node in node2dist:
                max_dist = max(node1dist[node], node2dist[node])
                if max_dist < min_dist:
                     min_dist = max_dist
                     ans = node
        return ans









        
