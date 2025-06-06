# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = start = end = 0
        char_count = defaultdict(int)
        
        while start <= end and end < len(s):
            if char_count[s[end]]:
                char_count[s[start]] -= 1
                start += 1
            else:
                char_count[s[end]] += 1
                res = max(res, end - start +1)
                end+=1
        return res
            
            



        
