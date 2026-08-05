# https://leetcode.com/problems/extra-characters-in-a-string/


from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Build trie
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

        n = len(s)
        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            if i == n:
                return 0

            # Option 1: s[i] is extra, move on
            best = dfs(i + 1) + 1
            
            # Option 2: walk the trie forward from i, matching any
            # dictionary word that starts at i
            node = root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_word:
                    best = min(best, dfs(j + 1))
            return best
        return dfs(0)

        
        
