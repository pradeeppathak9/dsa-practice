# https://leetcode.com/problems/maximum-frequency-stack/

from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.stack = []
        self.val_freq = defaultdict(int)
        self.freq_to_val = defaultdict(set)
        self.max_freq = 0

        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # updating hashmaps
        freq = self.val_freq[val]
        if freq != 0:
            self.freq_to_val[freq].remove(val)
        freq += 1
        self.val_freq[val] = freq
        self.freq_to_val[freq].add(val)
        self.max_freq = max(self.max_freq, freq)
        
        # print("push", val, freq, self.max_freq, self.freq_to_val, self.stack)
        return

    def pop(self) -> int:
        if self.max_freq == 0:
            return 
        for index in reversed(range(len(self.stack))):
            val = self.stack[index]
            if val in self.freq_to_val[self.max_freq]:
                break 
        self.stack = self.stack[:index] + self.stack[index + 1:] 
        
        # updating hashmaps
        self.val_freq[val] -= 1
        self.freq_to_val[self.max_freq].remove(val)
        if self.max_freq - 1:
            self.freq_to_val[self.max_freq - 1].add(val)

        if len(self.freq_to_val[self.max_freq]) == 0:
            self.max_freq -= 1 
        
        # print("pop", val, i, self.max_freq, self.freq_to_val, self.stack)
        return val
            
    

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
