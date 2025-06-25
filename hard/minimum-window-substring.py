# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        need = len(counter_t.keys())

        temp = defaultdict(int)
        have = 0

        l, r = 0, 0
        ans = None
        res = len(s) + 1
        while r < len(s):
            if s[r] in counter_t:
                temp[s[r]] += 1
                if temp[s[r]] == counter_t[s[r]]:
                    have += 1

            while have == need:
                if r - l + 1 < res:
                    res = r - l + 1
                    ans = (l, r)

                if s[l] in counter_t:
                    temp[s[l]] -= 1
                    if temp[s[l]] < counter_t[s[l]]:
                        have -= 1
                l += 1
            r += 1
        
        return s[ans[0]:ans[1] + 1] if ans else ""


