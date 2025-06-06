# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

# Union Find Solution
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        def find(c):
            if parent.get(c, c) == c:
                return c
            parent[c] = find(parent[c])
            return parent[c]

        def union(a, b):
            a, b = find(a), find(b)
            parent[a] = min(a, b)
            parent[b] = min(a, b)
            
        for a, b in zip(s1, s2):
            union(a, b)

        # print(parent)
        return "".join( find(c) for c in baseStr)


# DFS Solution
# class Solution:
#     def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
#         adj = defaultdict(list)

#         # Step 1: Build the graph
#         for a, b in zip(s1, s2):
#             adj[a].append(b)
#             adj[b].append(a)

#         def dfs(ch, visited):
#             visited.add(ch)
#             min_ch = ch
#             for nei in adj[ch]:
#                 if nei not in visited:
#                     candidate = dfs(nei, visited)
#                     min_ch = min(min_ch, candidate)
#             return min_ch

#         result = []
#         for ch in baseStr:
#             visited = set()
#             result.append(dfs(ch, visited))
        
#         return ''.join(result)
        

        

        
