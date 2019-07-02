class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.size = 0
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key >= self.size:
            for i in range(self.size, key + 1):
                self.array.append(-1)
                self.size = key + 1
        self.array[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key >= self.size:
            return -1
        return self.array[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key < self.size:
            self.array[key] = -1
