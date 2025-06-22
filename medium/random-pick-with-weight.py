# https://leetcode.com/problems/random-pick-with-weight

from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total
        print(self.prefix)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        # binary search
        return bisect.bisect_left(self.prefix, rand)
