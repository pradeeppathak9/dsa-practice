
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def solution(s):
    max_length = start = index = 0
    memo, result = {}, ""
    while index < len(s):
        c = s[index]
        if c in memo:
            start = index = memo[c] + 1
            memo = {}
            continue

        if max_length < index - start + 1:
            max_length = index - start + 1
            result = s[start:index + 1]
        memo[c] = index
        index += 1
    return max_length

s = "pwwkew"
print(solution(s))
