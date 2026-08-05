
# https://leetcode.com/problems/word-search-ii/

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicate results
            
            board[r][c] = '#'  # mark visited
            
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            board[r][c] = ch  # backtrack
            
            # Optimization: prune trie nodes with no remaining children (dead ends)
            if not next_node.children:
                del node.children[ch]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result
