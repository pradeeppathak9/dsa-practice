# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import defaultdict, Counter

def solution(s):
    count = Counter(s)
    bucket = defaultdict(set)
    for k, v in count.items():
        bucket[v].add(k)
        
    res = ''
    for freq in range(len(s), 0, -1):
        for c in bucket[freq]:
            for j in range(freq):
                res += c
    return res
        

