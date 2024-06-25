# https://leetcode.com/problems/group-anagrams/

def solution(strs):
    grp = defaultdict(list)
    for st in strs:
        grp[''.join(sorted(st))].append(st)

    res = [v for k, v in grp.items()  ]
    return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return solution(strs)
        
