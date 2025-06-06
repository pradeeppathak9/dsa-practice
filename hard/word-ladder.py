
# https://leetcode.com/problems/word-ladder

from collections import defaultdict, deque

def solution(beginWord, endWord, wordList):
    change_map = defaultdict(list)
    for w in wordList:
        for i in range(len(w)):
            change_map[ w[:i] + '*' + w[i+1:]].append(w)
    
    q = deque()
    q.append((beginWord, 1))
    visited = set()
    visited.add(beginWord)
    while len(q):
        w1, level = q.popleft()
        # print(w1, level, endWord)
        if w1 == endWord:
            return level

        for i in range(len(w1)):
            for w2 in change_map[ w1[:i] + '*' + w1[i+1:]]:
                if w2 not in visited:
                    visited.add(w2)
                    q.append((w2, level + 1))
    return 0


    

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return solution(beginWord, endWord, wordList)
        
        
