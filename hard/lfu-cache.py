# https://leetcode.com/problems/lfu-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def remove_tail(self):
        tail = self.tail.prev
        self.remove_node(tail)
        return tail

    def __str__(self):
        node = self.head.next
        res = []
        while node != self.tail:
            res.append(f'{node.key, node.value}')
            node = node.next
        return ' -> '.join(res)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.dll.remove_node(node)
            self.dll.insert_head(node)
            print(f"get - {key} - {self.dll}")
            return node.value
        else:
            return -1
  
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            del self.cache[key]
            self.dll.remove_node(node)
        else:
            node = Node(key, value)

        if self.capacity == len(self.cache):
            del self.cache[self.dll.tail.prev.key]
            self.dll.remove_node(self.dll.tail.prev)

        self.dll.insert_head(node)
        self.cache[key] = node
        print(f"put - {key} - {self.dll}")
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
