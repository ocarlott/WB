class ListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"Node with key {self.key} and value {self.value}"

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.filled = 0
        self.storage = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.storage:
            temp = self.storage[key]
            if not temp.next:
                return temp.value
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            else:
                self.tail = self.tail.next
            temp.prev = self.head
            self.head.next = temp
            temp.next = None
            self.head = temp
            return temp.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.head = self.tail = ListNode(key, value)
            self.storage[key] = self.head
            self.filled += 1
        else:
            if key in self.storage:
                self.storage[key].value = value
                self.get(key)
            else:
                self.head.next = ListNode(key, value)
                self.head.next.prev = self.head
                self.head = self.head.next
                self.storage[key] = self.head
                if self.filled == self.capacity:
                    temp = self.tail
                    self.tail = self.tail.next
                    self.tail.prev = None
                    del self.storage[temp.key]
                else:
                    self.filled += 1   
