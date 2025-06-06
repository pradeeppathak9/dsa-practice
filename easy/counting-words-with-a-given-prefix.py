# https://leetcode.com/problems/counting-words-with-a-given-prefix/

############## Solution with Prefix Tree
from collections import defaultdict

class PrefixNode: 
    def __init__(self):
        self.children = {}
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add(self, w):
        root = self.root
        for c in w:
            if c not in root.children:
                root.children[c] = PrefixNode()
            root = root.children[c]
            root.count += 1 


    def count(self, pref):
        root = self.root
        for c in pref:
            if c in root.children:
                root = root.children[c]
            else:
                return 0
        return root.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()
        for w in words:
            prefix_tree.add(w)
        return prefix_tree.count(pref)


############## Brute Force solution
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for w in words:
            if w.startswith(pref):
                ans +=1
        return ans
