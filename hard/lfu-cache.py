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
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
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

import collections 

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_table = collections.defaultdict(DLL)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.cache: 
            return self.update_cache(self.cache[key], key, self.cache[key].value)
        return -1

    
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache: 
            self.update_cache(self.cache[key], key, value)
        else:
            if len(self.cache) == self.capacity:
                # print(self.cache, self.min_freq)
                prev_tail = self.freq_table[self.min_freq].remove_tail()
                del self.cache[prev_tail.key]
            node = Node(key, value)
            self.freq_table[1].insert_head(node)
            self.cache[key] = node
            self.min_freq = 1

    def update_cache(self, node, key, value):
        node = self.cache[key]
        node.value = value
        prev_freq = node.freq
        node.freq += 1
        self.freq_table[prev_freq].remove_node(node)
        self.freq_table[node.freq].insert_head(node)

        if prev_freq == self.min_freq and self.freq_table[prev_freq].size == 0:
            self.min_freq += 1
        return node.value 





        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
