class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.size = 0
        

    def add(self, key: int) -> None:
        if key >= self.size:
            newSize = int(key * 1.3)
            for i in range(self.size, newSize + 1):
                self.array.append(False)
            self.size = newSize + 1
        self.array[key] = True
        
    def remove(self, key: int) -> None:
        if key < self.size:
            self.array[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key >= self.size:
            return False
        else:
            return self.array[key]
