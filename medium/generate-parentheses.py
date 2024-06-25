# https://leetcode.com/problems/generate-parentheses/

def solution(n, open_braces = 0, s='', result=[]):
    #     print(n, open_braces, s)
    if n < 0 or open_braces < 0:
        return result
    if n == 0 and open_braces == 0:
        result.append(s)
        return result

    result = solution(n - 1, open_braces+1, s + '(', result)
    result = solution(n, open_braces - 1, s + ')', result)
    return result

print(solution(3))
