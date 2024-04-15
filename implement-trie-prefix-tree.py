# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = ''

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '*' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)






# class Node: 
#     def __init__(self):
#         self.children = {}
#         self.end = False

# class Trie:

#     def __init__(self):
#         self.trie = Node()

#     def insert(self, word: str) -> None:
#         node = self.trie
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = Node()
#             node = node.children[c]
#         node.end = True

#     def search(self, word: str) -> bool:
#         node = self.trie
#         for c in word:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return node.end

#     def startsWith(self, prefix: str) -> bool:
#         node = self.trie
#         for c in prefix:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return True
