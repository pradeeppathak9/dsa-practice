# https://leetcode.com/problems/replace-words/

def solution(dictionary, sentence):
    dictionary = set(dictionary)
    words = sentence.split(" ")
    res = []
    for w in words:
        for i in range(len(w)):
            if w[:i] in dictionary:
                w = w[:i]
                break
        res.append(w)
    return " ".join(res)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        return solution(dictionary, sentence)
        
