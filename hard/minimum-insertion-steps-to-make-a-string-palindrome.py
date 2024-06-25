# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

def solution(s, changes=0, memo={}):
    n = len(s)
    i, j = 0, len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
        
    if i >= j: 
        return 0
    
    sub = s[i:j+1]
    if sub in memo:
        return memo[sub]
    
    res = min(
        solution(sub + s[i], changes, memo),
        solution(s[j] + sub, changes, memo),
    )
    memo[sub] = res + 1
    return res + 1
    
        
        
s = 'leetcode'        
s = 'mbadm'
s = 'zzazz'
s = 'jsdaaaaaaaaxghjj'
s = "tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"
s = "zjveiiwvc"

print(solution(s))
