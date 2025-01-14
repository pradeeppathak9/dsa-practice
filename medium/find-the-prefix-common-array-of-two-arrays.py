# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/


from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_count = defaultdict(int)
        b_count = defaultdict(int)
        C = [0] * (len(A) + 1)
        for i in range(len(A)):
            if A[i] == B[i]:
                C[i+1] = C[i] + 1
            else:
                C[i+1] = C[i] \
                + int(a_count[A[i]] < b_count[A[i]]) \
                + int(b_count[B[i]] < a_count[B[i]])
            a_count[A[i]] += 1
            b_count[B[i]] += 1
            
        return C[1:]
