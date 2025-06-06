# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

class Solution:
    def robotWithString(self, s: str) -> str:
        min_char_to_right = [s[-1]] * len(s)
        for i in range(len(s) - 2, -1, -1):
            min_char_to_right[i] = min(min_char_to_right[i + 1], s[i])
        
        t, p = [], []
        for i, c in enumerate(s):
            t.append(c)
            min_char = min_char_to_right[i + 1] if i + 1 < len(s) else s[i] 
            while len(t) and t[-1] <= min_char :
                p.append(t.pop())
                
        while len(t):
            p.append(t.pop())

        return "".join(p)



   

