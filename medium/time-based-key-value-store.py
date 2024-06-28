# https://leetcode.com/problems/time-based-key-value-store/



from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hist = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hist[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hist.get(key, [])
        l, r = 0, len(values) -1
        ans = ""
        while l <= r:
            mid = (l + r) >> 1
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1 
        return ans        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
