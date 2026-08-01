# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        
        if start in dead:
            return -1
        if target == start:
            return 0

        def neighbors(state):
            for i in range(4):
                digit = int(state[i])
                for d in (-1, 1):
                    new_digit = (digit + d) % 10
                    yield state[:i] + str(new_digit) + state[i+1:]

        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            state, steps = queue.popleft()
            for nxt in neighbors(state):
                if nxt == target:
                    return steps + 1
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
                    
        return -1


        
