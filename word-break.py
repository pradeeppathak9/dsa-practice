# https://leetcode.com/problems/word-break/ 

def solution(s, wordDict):
    dp = [False for i in range(len(s) + 1)]
    max_len = max(map(len, wordDict))
    dp[0] = True

    for i in range(0, len(s) + 1):
        for j in range(i+1, min(i+1 + max_len, len(s) + 1)):
            if not dp[j]:
                dp[j] = dp[i] and s[i:j] in wordDict
    # print(dp)
    return dp[-1]


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
assert solution(s, wordDict) == False

s = "leetcode"
wordDict = ["leet", "code"]
assert solution(s, wordDict) == True

s = "applepenapple"
wordDict = ["apple","pen"]
assert solution(s, wordDict) == True

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
assert solution(s, wordDict) == False
