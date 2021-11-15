# https://leetcode.com/problems/longest-valid-parentheses

def solution(s):
    from collections import deque

    dp = [0] *len(s)    
    stack = deque()
    for index, c in enumerate(s):
        if c == ')':
            if len(stack):
                dp[index] = 1
                dp[stack.pop()] = 1
        else:
            stack.append(index)
    print(dp)

    counter = res = 0        
    for v in dp:
        counter = counter*v + v
        res = max(counter, res)
    return res


s = ")())()()())(())"
print(solution(s))
