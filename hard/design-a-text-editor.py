# https://leetcode.com/problems/design-a-text-editor/


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node("#", None)
        self.tail = Node("$", None)
        self.cursor = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_at_cursor(self, node):
        node.next = self.cursor.next
        node.prev = self.cursor
        self.cursor.next.prev = node
        self.cursor.next = node
        self.cursor = self.cursor.next
        self.size += 1

    def delete_at_cusrsor(self):
        if self.cursor == self.head:
            return False
        prev = self.cursor.prev
        self.cursor.next.prev = self.cursor.prev
        self.cursor.prev.next = self.cursor.next
        self.cursor = prev
        return True

    def cursor_left(self):
        if self.cursor != self.head:
            self.cursor = self.cursor.prev

    def cursor_right(self):
        if self.cursor.next != self.tail:
            self.cursor = self.cursor.next
        
    def cursor_print(self, k=10):
        node = self.cursor
        res = []
        while node != self.head and k != 0:
            res.append(f'{node.key}')
            k -= 1
            node = node.prev
        return ''.join(res[::-1])
        

    def __str__(self):
        node = self.head
        res = []
        while node:
            res.append(f'{node.key}')
            if node == self.cursor:
                res.append(f'|')
            node = node.next
        return ''.join(res)

class TextEditor:

    def __init__(self):
        self.dll = DLL()
        
    def addText(self, text: str) -> None:
        for c in text:
            node = Node(c, c)
            self.dll.insert_at_cursor(node)
        # print(f"addText {self.dll} - {text}")

    def deleteText(self, k: int) -> int:
        count = 0
        for i in range(k):
            if self.dll.delete_at_cusrsor():
                count += 1
        # print(f"deleteText {self.dll} - {count}")
        return count 

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            self.dll.cursor_left()
        # print(f"cursorLeft {self.dll} - {k} - {self.dll.cursor_print()}")
        return self.dll.cursor_print()

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            self.dll.cursor_right()
        # print(f"cursorRight {self.dll} - {k} - {self.dll.cursor_print()}")
        return self.dll.cursor_print()
        
        

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
