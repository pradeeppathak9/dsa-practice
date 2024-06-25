# https://leetcode.com/problems/all-oone-data-structure/

class ListNode: 
    def __init__(self, count: int = -1):
        self.prev = None
        self.next = None
        self.words = set()
        self.count = count

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_word(self, node: ListNode, word:str) -> None:
        node.words.remove(word)
        if not node.words:
            self.remove_node(node)
    
    def remove_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_right_node(self, current_node: ListNode, new_node: ListNode) -> None:
        new_node.next = current_node.next
        current_node.next.prev = new_node
        new_node.prev = current_node
        current_node.next = new_node

    
class AllOne:

    def __init__(self):
        self.word_to_node = {}
        self.dll = DoubleLinkedList()
        

    def inc(self, key: str) -> None:
        if key in self.word_to_node:
            current_node = self.word_to_node[key]
            count = current_node.count + 1
            next_node = current_node.next

            if next_node.count != count: 
                next_node = ListNode(count)
                self.dll.add_right_node(current_node, next_node)
            

            next_node.words.add(key)
            self.word_to_node[key] = next_node
            self.dll.remove_word(current_node, key)
        else:
            head = self.dll.head
            next_node = head.next

            if next_node.count != 1:
                next_node = ListNode(1)
                self.dll.add_right_node(head, next_node)
            
            next_node.words.add(key)
            self.word_to_node[key] = next_node


    def dec(self, key: str) -> None:
        current_node = self.word_to_node[key]
        count = current_node.count - 1
        if count == 0:
            del self.word_to_node[key]
        else:
            prev_node = current_node.prev
            if prev_node.count != count:
                next_node = ListNode(count)
                self.dll.add_right_node(prev_node, next_node)
            else:
                next_node = prev_node

            next_node.words.add(key)
            self.word_to_node[key] = next_node
        self.dll.remove_word(current_node, key)

    def getMaxKey(self) -> str:
        words = self.dll.tail.prev.words
        if words:
            word = words.pop()
            words.add(word)
            return word
        return ""
        
    def getMinKey(self) -> str:
        words = self.dll.head.next.words
        if words:
            word = words.pop()
            words.add(word)
            return word
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
