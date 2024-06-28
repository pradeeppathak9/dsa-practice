# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node_mapping = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        return

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        return 

    def get(self, key: int) -> int:
        if key in self.key_node_mapping:
            node = self.key_node_mapping[key]
            self.delete_node(node)
            self.add_node_to_front(node)
            return node.value
        else:
            return -1
        # self.chache_status()
  
    def put(self, key: int, value: int) -> None:
        if key in self.key_node_mapping:
            node = self.key_node_mapping[key]
            node.value = value
            del self.key_node_mapping[key]
            self.delete_node(node)
        else:
            node = Node(key, value)

        if self.capacity == len(self.key_node_mapping):
            del self.key_node_mapping[self.tail.prev.key]
            self.delete_node(self.tail.prev)

        self.add_node_to_front(node)
        self.key_node_mapping[key] = node
        # self.chache_status()
        return

    def chache_status(self):
            trav = self.head.next
            res = []
            while trav != self.tail:
                res.append((trav.key, trav.value))
                trav = trav.next
            print(res, self.key_node_mapping.keys())



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
