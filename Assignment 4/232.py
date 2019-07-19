class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.array.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = []
        while len(self.array) != 1:
            temp.append(self.array.pop())
        result = self.array.pop()
        while len(temp) != 0:
            self.array.append(temp.pop())
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.array[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.array) == 0
