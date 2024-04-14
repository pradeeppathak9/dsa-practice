
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# def solution(s):
#     max_length = start = index = 0
#     memo, result = {}, ""
#     while index < len(s):
#         c = s[index]
#         if c in memo:
#             start = index = memo[c] + 1
#             memo = {}
#             continue

#         if max_length < index - start + 1:
#             max_length = index - start + 1
#             result = s[start:index + 1]
#         memo[c] = index
#         index += 1
#     return max_length

# s = "pwwkew"
# print(solution(s))


from collections import defaultdict
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
            
