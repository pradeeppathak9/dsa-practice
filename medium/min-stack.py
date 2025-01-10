# https://leetcode.com/problems/min-stack/

class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        return 
        
    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
    
    def popMin(self) -> int:
        temp_stack = []
        while True: 
            val = self.stack.pop()
            if val != self.min_stack[-1]:
                temp_stack.append(val)
            else:
                break
        while len(temp_stack):
            self.stack.append(temp_stack.pop())
        return self.min_stack.pop()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
