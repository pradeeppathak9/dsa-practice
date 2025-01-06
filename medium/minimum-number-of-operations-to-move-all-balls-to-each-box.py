# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        left_1s, right_1s = 0, 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                res[0] += i
                right_1s += 1
        
        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                left_1s += 1
                right_1s -= 1
            res[i] = res[i-1] - right_1s + left_1s
        return res
