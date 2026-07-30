# https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = Node(None)
        self.k = k 
        self.n = 0 

    def enQueue(self, value: int) -> bool:
        if self.n == self.k:
            return False
        node = Node(value)
        self.rear.next = node
        self.rear = node
        self.n += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        self.n -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.rear == self.front
        
    def isFull(self) -> bool:
        return self.n == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
