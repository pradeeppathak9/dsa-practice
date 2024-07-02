# https://leetcode.com/problems/online-election/

from collections import defaultdict

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        vote_count = defaultdict(int)
        
        self.times = times
        vote_count[persons[0]] += 1
        self.leading = [ persons[0] ]
      
        for i in range(1, len(persons)):
            vote_count[persons[i]] += 1
            if vote_count[persons[i]] >= vote_count[self.leading[-1]]:
                self.leading.append(persons[i])
            else:
                self.leading.append(self.leading[-1])
        return 

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        while l < r:
            m =  (l + r) // 2
            if self.times[m] > t:
                r = m - 1
            else:
                l = m + 1
        if self.times[l] > t:
            l -= 1
        return self.leading[l]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
