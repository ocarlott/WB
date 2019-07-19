class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.array.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = []
        for i in range(len(self.array) - 1):
            temp.append(self.array[i])
        result = self.array[-1]
        self.array = temp
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.array[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.array) == 0
