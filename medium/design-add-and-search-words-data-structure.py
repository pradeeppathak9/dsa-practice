# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node: 
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Node()
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            
            if word[i] not in node.children:
                return False            
                
            return dfs(node.children[word[i]], i+1)
        return dfs(self.trie, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
