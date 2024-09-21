# https://leetcode.com/problems/lexicographical-numbers/


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        while len(result) < n: 
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else: 
                while curr == n or curr % 10 == 9:
                    curr //= 10
                curr += 1
        return result

        
        def dfs(curr):
            if curr > n:
                return 
            result.append(curr)
            for i in range(10):
                dfs(curr * 10 + i)
        for i in range(1, 10):
            dfs(i)
        return result 






