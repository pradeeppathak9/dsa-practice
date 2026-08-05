# https://leetcode.com/problems/word-break-ii

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        # Build trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.is_word = True

        n = len(s)
        memo = {}  # i -> list of valid sentences for s[i:]

        def dfs(i: int) -> list[str]:
            if i == n:
                return [""]  # one way to break the empty suffix: the empty sentence
            if i in memo:
                return memo[i]

            results = []
            node = root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_word:
                    word = s[i:j + 1]
                    for rest in dfs(j + 1):
                        results.append(word if not rest else word + " " + rest)

            memo[i] = results
            return results

        return dfs(0)
