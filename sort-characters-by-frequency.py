# https://leetcode.com/problems/sort-characters-by-frequency/


from collections import defaultdict

def solution(s):
    count = defaultdict(int)
    for c in s:
        count[c] += 1
        
    freq_count = defaultdict(set)
    for k, v in count.items():
        freq_count[v].add(k)
        
    
    res = ''
    for freq in range(len(s), 0, -1):
        for c in freq_count[freq]:
            for j in range(freq):
                res += c
    return res
        

